#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES_DIR = ROOT / "exercises"
DEFAULT_SOURCE = ROOT / "student" / "solution.cpp"


def normalize_text(value: str) -> str:
    return value.replace("\r\n", "\n").strip()


def generate_runner_cpp(source_file: Path) -> str:
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
    while (getline(input_file, line)) {{
        if (line.empty()) {{
            continue;
        }}

        istringstream iss(line);
        vector<int> arr;
        int value;
        while (iss >> value) {{
            arr.push_back(value);
        }}

        if (!arr.empty()) {{
            cout << find_max(arr) << '\\n';
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
    runner_cpp = binary_dir / f"{exercise_dir.name}_runner.cpp"
    runner_cpp.write_text(generate_runner_cpp(source_file), encoding="utf-8")

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

    try:
        binary_path = compile_runner(source_file, exercise_dir, binary_dir)
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Grade C++ array exercises from .txt tests.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Path to the student's C++ source file.")
    parser.add_argument("--exercise", type=Path, help="Optional path to one exercise directory, e.g. exercises/day_01")
    args = parser.parse_args()

    if not args.source.exists():
        print(f"Student source not found: {args.source}")
        return 1

    exercise_dirs = []
    if args.exercise:
        exercise_dirs = [args.exercise.resolve()]
    else:
        exercise_dirs = sorted([path for path in EXERCISES_DIR.iterdir() if path.is_dir()])

    if not exercise_dirs:
        print(f"No exercise directories found under {EXERCISES_DIR}")
        return 1

    overall_ok = True
    for exercise_dir in exercise_dirs:
        print(f"\n[INFO] Grading {exercise_dir.name}")
        try:
            ok, report = grade_exercise(exercise_dir, args.source)
        except Exception as exc:
            print(f"[ERROR] {exercise_dir.name}: {exc}")
            overall_ok = False
            continue

        if ok:
            for line in report:
                print(f"[PASS] {line}")
        else:
            for line in report:
                print(f"[FAIL] {line}")
            overall_ok = False

    if overall_ok:
        print("\nAll exercises passed.")
        return 0

    print("\nSome exercises failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
