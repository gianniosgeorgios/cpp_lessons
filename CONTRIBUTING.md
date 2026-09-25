# Contributing & Student Instructions

Instructor workflow:
- Add exercises under `exercises/<exercise-id>/` with `description.md` and a `tests/` folder containing paired `inputN.txt` and `expectedN.txt`.
- Push to GitHub; GitHub Actions will run the grader for submissions.


Student workflow (single-student, no git CLI required):

1. Open the repository in VSCode (clone or open the folder).
2. Use the Explorer to open `student/` and create a file named `<exercise-id>.c` (for example `ex01.c`). You can copy `template/solution.c` into `student/ex01.c` and edit it.
3. Use the VSCode Source Control view (left sidebar) to stage and commit your change.
4. Click the `...` menu in the Source Control view and choose `Push` (or use the `Publish Branch` / `Push` button). You can also use the GitHub Pull Requests extension to create a PR if required by the instructor.
5. The GitHub Actions grader will run on pushes that change `student/**` or `submissions/**` and post results in the Actions tab.

Notes:
- Use filenames `student/<exercise-id>.c` (e.g. `student/ex01.c`).
- Submission folders: teacher-created exercises use a date-based `exercise_id` (example: `050826` for 05-Aug-26). Student or submissions should be placed under `submissions/<exercise_id>/` and include one `.c` file named `task.c` (i.e. `submissions/050826/task.c`).
- Teacher provides a skeleton header `exercises/<exercise_id>/skeleton.h` and test drivers `exercises/<exercise_id>/tests/driverN.c` which will be compiled together with the student's `task.c`.
- The grader compiles with `gcc -std=c11 -O2` using `-I exercises/<exercise_id>` so drivers can `#include "skeleton.h"`.
- This workflow is designed for a single student editing files directly in `student/` with VSCode UI, or multiple students using the `submissions/` layout.
