# Array Exercises (C) — Student Submissions via GitHub

This repository hosts daily array exercises in C (target complexity O(N)). It's designed to be hosted publicly on GitHub (Pages) and to accept student submissions via pull requests. CI (GitHub Actions) automatically compiles and tests submitted programs against provided testcases.

Teacher workflow
- Add a new exercise folder under `exercises/dayNN/` with:
  - `statement.md` — problem text and constraints
  - `tests/inputX.txt` and `tests/outputX.txt` — paired testcases (X starts at 1)
- Commit and push to the `main` branch (or a branch deployed to Pages).

Student workflow
- Fork the repo and create a pull request adding your solution under `submissions/<github-username>/dayNN.c`.
- The CI will run and report test results on the PR. Keep outputs deterministic (no prompts).

For students (no git CLI required)

- You do NOT need to learn the git command-line. Use GitHub's web interface only:
  1. Fork the repository (click "Fork" in the top-right on GitHub).
  2. In your fork, click "Add file" → "Create new file".
  3. Name the file: `submissions/<your-github-username>/dayNN.c` (example: `submissions/alice/day1.c`).
  4. Paste your C source code into the editor.
  5. Commit the new file to your fork (provide a short commit message).
  6. Click the "Contribute" / "Pull request" button to open a PR back to the teacher's repository.

- The repository's CI will automatically compile and test your program on the PR. Fix any failing tests and push new commits from the web editor as needed.

- Requirements for solutions:
  - Read input from standard input and write result to standard output.
  - Do not print prompts or extra text — only the expected result(s).
  - Aim for O(n) time complexity as stated in each exercise.

Test online then upload (no CLI)

- Recommend online C editors where students can paste, run, and test code before uploading:
  - https://onlinegdb.com/online_c_compiler
  - https://replit.com/~ (choose C)
  - https://ideone.com/
  - https://wandbox.org/

- Quick testing steps (example using OnlineGDB):
  1. Open the online editor (e.g., OnlineGDB).
  2. Set language to C and paste your source code.
  3. To test with a provided testcase, open the program's stdin/input box and paste the input from the exercise `tests/inputX.txt`.
  4. Run the program and verify the output exactly matches the expected `tests/outputX.txt` (no extra text or prompts).
  5. If the editor offers a download button, download the `.c` file. Otherwise copy the source code text.

- Uploading your tested code (no command-line git):
  - Option A — Upload a file: In the teacher's repository on GitHub, click `Add file` → `Upload files`, then upload a file named `submissions/<your-github-username>/dayNN.c`.
  - Option B — Create new file: In your fork (or the teacher repo if allowed) click `Add file` → `Create new file`. Use the path `submissions/<your-github-username>/dayNN.c`, paste your code, and commit.
  - After adding the file in your fork, open a Pull Request back to the teacher's repository so CI can run automatically.

- Important: the file must have a `.c` extension and follow the input/output contract in the exercise. If tests fail, edit the file in your fork using the web editor and push a new commit via the web UI.

How CI works
- On each pull request, the workflow compiles each submitted `.c` file and runs it against all tests found in the corresponding exercise folder. If any test fails, the job fails and CI reports which test failed.

Local testing
You can run the `scripts/test_submission.sh` locally to verify a submission before opening a PR:

```bash
chmod +x scripts/test_submission.sh
./scripts/test_submission.sh submissions/example/day1.c exercises/day1
```

License: Use as you wish.

Student submission page (one-click)
- To provide a friendly UI for students who do not use the command line, we include `student_submit.html`. Host this file via GitHub Pages (or open it locally) and students can:
  - Paste code they already tested in an online C editor.
  - Enter their GitHub username and click "Open GitHub New-File Editor".
  - The teacher repo's new-file editor opens pre-filled with filename and source so the student can commit via the GitHub web UI.

This avoids any git commands while still letting the CI test submissions via PRs.

