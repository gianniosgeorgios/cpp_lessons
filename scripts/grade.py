#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ex_dir = ROOT / 'exercises'
subs_dir = ROOT / 'submissions'
student_dir = ROOT / 'student'

def run(cmd, input_data=None, timeout=5):
    try:
        p = subprocess.run(cmd, input=input_data, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, '', 'TIMEOUT'

def grade_submission(cpath, exid):
    """
    Compile tests/driverN.c together with the student's cpath.
    Drivers must `#include "skeleton.h"` and we add -I exercises/<exid>.
    Fallback: if there are no driverN.c files, compile the student's file directly.
    """
    details = []
    tests_dir = ex_dir/exid/'tests'
    drivers = sorted(tests_dir.glob('driver*.c')) if tests_dir.exists() else []
    all_ok = True

    if drivers:
        for drv in drivers:
            num = drv.stem.replace('driver','')
            inp = tests_dir/f'input{num}.txt'
            expected = tests_dir/f'expected{num}.txt'
            if not inp.exists() or not expected.exists():
                details.append(f'Missing input/expected for driver {drv.name}')
                all_ok = False
                continue
            binpath = Path(str(cpath) + f'.{num}.bin')
            cmd = ['gcc','-std=c11','-O2',str(drv),str(cpath),'-I',str(ex_dir/exid),'-o',str(binpath)]
            rc, so, se = run(cmd)
            if rc != 0:
                details.append(f'compile error for driver {drv.name}:\n{se}')
                all_ok = False
                continue
            with inp.open('r') as f:
                data = f.read()
            rc, so, se = run([str(binpath)], input_data=data, timeout=2)
            if rc != 0:
                details.append(f'Runtime error for {drv.name}: exit {rc} stderr:\n{se}')
                all_ok = False
                continue
            got = so.strip()
            want = expected.read_text().strip()
            if got != want:
                all_ok = False
                details.append(f'Test {drv.name} failed:\n got: {got!r}\n want:{want!r}')
            else:
                details.append(f'Test {drv.name} OK')
    else:
        # fallback: compile student's file alone
        binpath = cpath.with_suffix('')
        rc, so, se = run(['gcc','-std=c11','-O2',str(cpath),'-o',str(binpath)])
        if rc != 0:
            return False, f'compile error:\n{se}'
        tests = sorted((tests_dir).glob('input*.txt')) if tests_dir.exists() else []
        if not tests:
            return False, 'no tests found'
        for inp in tests:
            num = inp.stem.replace('input','')
            expected = inp.parent/f'expected{num}.txt'
            if not expected.exists():
                details.append(f'Missing expected for {inp.name}')
                all_ok = False
                continue
            with inp.open('r') as f: data = f.read()
            rc, so, se = run([str(binpath)], input_data=data, timeout=2)
            if rc != 0:
                details.append(f'Runtime error for {inp.name}: exit {rc} stderr:\n{se}')
                all_ok = False
                continue
            got = so.strip()
            want = expected.read_text().strip()
            if got != want:
                all_ok = False
                details.append(f'Test {inp.name} failed:\n got: {got!r}\n want:{want!r}')
            else:
                details.append(f'Test {inp.name} OK')

    return all_ok, '\n'.join(details)

def main():
    any_fail = False

    # Grade submissions/ (multiple students) if present
    if subs_dir.exists():
        for ex in sorted(subs_dir.iterdir()):
            if not ex.is_dir():
                continue
            exid = ex.name
            for cfile in sorted(ex.glob('*.c')):
                print(f'Grading {cfile} (exercise {exid})')
                ok, details = grade_submission(cfile, exid)
                print(details)
                if not ok:
                    any_fail = True

    # Also grade single-student files in student/<exercise-id>.c
    if student_dir.exists():
        for ex in sorted(ex_dir.iterdir()):
            if not ex.is_dir():
                continue
            exid = ex.name
            candidate = student_dir / f'{exid}.c'
            if candidate.exists():
                print(f'Grading {candidate} (exercise {exid})')
                ok, details = grade_submission(candidate, exid)
                print(details)
                if not ok:
                    any_fail = True
    if any_fail:
        print('\nOne or more submissions failed')
        sys.exit(2)
    print('\nAll graded submissions passed')

if __name__=='__main__':
    main()
