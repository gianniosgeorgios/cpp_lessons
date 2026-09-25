# C++ Array Exercise Lab

This repository is designed for a teacher-student workflow where each day a new array problem is posted and the student solves it in C++.

The key idea is simple:
- the student writes code in `student/solution.cpp`
- tests live in `exercises/<day_name>/tests/*.txt`
- the grader reads `.txt` input/output files and compares the program output
- GitHub Actions runs automatically on push, so the student can see if the solution is passing or failing without a local debugger

## Recommended workflow

1. Open the project in VS Code.
2. Edit the student solution in `student/solution.cpp`.
3. Run the checker locally:
   `python3 scripts/grade.py`
4. Commit and push the changes:
   `git add .`
   `git commit -m "Solve day 01"`
   `git push`
5. GitHub Actions will run the same grader in the cloud and show a green or red check.

## Project layout

- `student/solution.cpp` – current student solution
- `exercises/` – one folder per daily exercise
- `scripts/grade.py` – local and CI grading script
- `.github/workflows/grade.yml` – GitHub Action that runs the grader automatically

## Exercise format

Each exercise folder should look like this:

```text
exercises/
  day_01/
    README.md
    tests/
      input.txt
      output.txt
```

The `input.txt` file contains one array per line.
The `output.txt` file contains the expected result for each array on the same line number.

Example:

```text
input.txt
3 8 1 9 4 12 5 7
5 -4 -9 -3 -1 -7
```

```text
output.txt
12
-1
```

The grader reads each line from the input file, calls the student function, and compares the output line-by-line.

## Complexity target

All exercises in this repo are array-based and expected to be solved in O(N) time.

That means the student should usually:
- iterate through the array only once
- avoid nested loops
- avoid repeated scans unless the problem explicitly requires it

## Sample exercise included

A sample exercise is already present:
- `exercises/day_01/`

It asks for the maximum value in an array in O(N) time.

## Teacher notes

To add a new daily challenge:
1. create a new folder under `exercises/`
2. write a short problem description in `README.md`
3. add `input.txt` and `output.txt` files
4. tell the student to solve in `student/solution.cpp`
5. commit and push

The grader will automatically discover the tests and run them.
