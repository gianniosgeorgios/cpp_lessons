#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES_DIR = ROOT / "exercises"
DEFAULT_SOURCE = ROOT / "student" / "solution.cpp"


def resolve_student_source(exercise_dir: Path, source_file: Path | None) -> Path:
    if source_file is not None:
        if not source_file.exists():
            raise FileNotFoundError(f"Student source not found: {source_file}")
        return source_file

    day_solution = ROOT / "student" / exercise_dir.name / "solution.cpp"
    if day_solution.exists():
        return day_solution

    if DEFAULT_SOURCE.exists():
        return DEFAULT_SOURCE

    raise FileNotFoundError(f"No student source found for {exercise_dir.name}")


def normalize_text(value: str) -> str:
    return value.replace("\r\n", "\n").strip()


def read_function_name(exercise_dir: Path) -> str:
    function_file = exercise_dir / "function_name.txt"
    if function_file.exists():
        name = function_file.read_text(encoding="utf-8").strip()
        if name:
            return name

    return "find_max"


def generate_runner_cpp(source_file: Path, function_name: str) -> str:
    source_include = source_file.as_posix()
    return f'''#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define main student_main
#include "{source_include}"
#undef main

using namespace std;

int main(int argc, char** argv) {{
    if (argc < 2) {{
        return 1;
    }}

    ifstream input_file(argv[1]);
    if (!input_file) {{
        return 2;
    }}

    string line;
    int N;
    while (getline(input_file, line)) {{
        if (line.empty()) {{
            continue;
        }}
        
        // Parse N from first line
        istringstream iss_n(line);
        if (!(iss_n >> N) || N <= 0) {{
            continue;
        }}
        
        // Parse array from second line (comma-separated)
        if (!getline(input_file, line)) {{
            break;
        }}
        
        vector<int> arr;
        istringstream iss(line);
        string token;
        while (getline(iss, token, ',')) {{
            try {{
                arr.push_back(stoi(token));
            }} catch (...) {{
                continue;
            }}
        }}
        
        if (static_cast<int>(arr.size()) == N) {{
            cout << {function_name}(N, arr.data()) << '\\n';
        }}
    }}

    return 0;
}}
'''


def collect_cases(exercise_dir: Path):
    tests_dir = exercise_dir / "tests"
    if not tests_dir.exists():
        raise FileNotFoundError(f"Missing tests folder for {exercise_dir.name}: {tests_dir}")

    input_file = tests_dir / "input.txt"
    output_file = tests_dir / "output.txt"
    if input_file.exists() and output_file.exists():
        return [(input_file, output_file)]

    input_cases = sorted(tests_dir.glob("input_*.txt"))
    if not input_cases:
        raise FileNotFoundError(f"No input.txt or input_*.txt files found in {tests_dir}")

    cases = []
    for input_case in input_cases:
        suffix = input_case.stem.replace("input_", "")
        expected_file = tests_dir / f"output_{suffix}.txt"
        if not expected_file.exists():
            raise FileNotFoundError(f"Missing expected output for {input_case.name}: {expected_file}")
        cases.append((input_case, expected_file))

    return cases


def compile_runner(source_file: Path, exercise_dir: Path, binary_dir: Path) -> Path:
    function_name = read_function_name(exercise_dir)
    runner_cpp = binary_dir / f"{exercise_dir.name}_runner.cpp"
    runner_cpp.write_text(generate_runner_cpp(source_file, function_name), encoding="utf-8")

    binary_path = binary_dir / f"{exercise_dir.name}_runner.out"
    compile_result = subprocess.run(
        [
            "g++",
            "-std=c++17",
            "-O2",
            "-Wall",
            "-Wextra",
            str(runner_cpp),
            "-o",
            str(binary_path),
        ],
        capture_output=True,
        text=True,
    )

    if compile_result.returncode != 0:
        details = compile_result.stderr.strip() or compile_result.stdout.strip()
        raise RuntimeError(f"Compile failed for {exercise_dir.name}:\n{details}")

    return binary_path


def grade_exercise(exercise_dir: Path, source_file: Path) -> tuple[bool, list[str]]:
    report = []
    tests_dir = exercise_dir / "tests"
    binary_dir = ROOT / ".grade"
    binary_dir.mkdir(exist_ok=True)

    actual_source = resolve_student_source(exercise_dir, source_file)

    try:
        binary_path = compile_runner(actual_source, exercise_dir, binary_dir)
    except RuntimeError as exc:
        return False, [str(exc)]

    cases = collect_cases(exercise_dir)
    all_passed = True

    for input_file, expected_file in cases:
        if input_file.name == "input.txt" and expected_file.name == "output.txt":
            run_result = subprocess.run([str(binary_path), str(input_file)], capture_output=True, text=True, check=False)
            if run_result.returncode != 0:
                report.append(f"Runtime error for {exercise_dir.name}:\n{run_result.stderr.strip() or run_result.stdout.strip() or 'unknown runtime error'}")
                all_passed = False
                continue

            actual_output = normalize_text(run_result.stdout)
            expected_output = normalize_text(expected_file.read_text(encoding="utf-8"))

            if actual_output != expected_output:
                report.append(
                    "Output mismatch for "
                    f"{exercise_dir.name}:\nExpected:\n{expected_output}\n\nActual:\n{actual_output}"
                )
                all_passed = False
            else:
                report.append(f"PASS: {exercise_dir.name} ({input_file.name})")
            continue

        run_result = subprocess.run([str(binary_path), str(input_file)], capture_output=True, text=True, check=False)
        if run_result.returncode != 0:
            report.append(f"Runtime error for {exercise_dir.name} ({input_file.name}):\n{run_result.stderr.strip() or run_result.stdout.strip() or 'unknown runtime error'}")
            all_passed = False
            continue

        actual_output = normalize_text(run_result.stdout)
        expected_output = normalize_text(expected_file.read_text(encoding="utf-8"))

        if actual_output != expected_output:
            report.append(
                "Output mismatch for "
                f"{exercise_dir.name} ({input_file.name}):\nExpected:\n{expected_output}\n\nActual:\n{actual_output}"
            )
            all_passed = False
        else:
            report.append(f"PASS: {exercise_dir.name} ({input_file.name})")

    return all_passed, report


def read_days_config(days_file: Path) -> list[str]:
    """Read which days should be graded from days.txt"""
    if not days_file.exists():
        return []
    
    days = []
    for line in days_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            days.append(line)
    return days


def main() -> int:
    parser = argparse.ArgumentParser(description="Grade C++ array exercises from .txt tests.")
    parser.add_argument("--source", type=Path, help="Optional override path to the student's C++ source file.")
    parser.add_argument("--exercise", type=Path, help="Optional path to one exercise directory, e.g. exercises/day_01")
    args = parser.parse_args()

    if args.source is not None and not args.source.exists():
        print(f"Student source not found: {args.source}")
        return 1

    exercise_dirs = []
    if args.exercise:
        exercise_dirs = [args.exercise.resolve()]
    else:
        # Read which days to grade from days.txt
        days_config_file = ROOT / "days.txt"
        specified_days = read_days_config(days_config_file)
        
        if specified_days:
            # Only grade specified days
            for day in specified_days:
                day_path = EXERCISES_DIR / day
                if day_path.exists() and day_path.is_dir():
                    exercise_dirs.append(day_path)
        else:
            # If no days.txt or empty, grade all days
            exercise_dirs = sorted([path for path in EXERCISES_DIR.iterdir() if path.is_dir()])

    if not exercise_dirs:
        print(f"No exercise directories found under {EXERCISES_DIR}")
        return 1

    # Process single day
    exercise_dir = exercise_dirs[0]
    print(f"\n[INFO] Grading {exercise_dir.name}")
    try:
        source_to_use = resolve_student_source(exercise_dir, args.source)
        ok, report = grade_exercise(exercise_dir, source_to_use)
    except Exception as exc:
        print(f"[ERROR] {exercise_dir.name}: {exc}")
        return 1

    if ok:
        for line in report:
            print(f"[PASS] {line}")
        print(f"\n{exercise_dir.name} passed.")
        return 0
    else:
        for line in report:
            print(f"[FAIL] {line}")
        print(f"\n{exercise_dir.name} failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
