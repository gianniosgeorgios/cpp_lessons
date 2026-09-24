#!/usr/bin/env bash
set -euo pipefail

# If arguments provided: test that specific submission against given exercise
if [ "$#" -ge 2 ]; then
  SUBFILES=("$1")
  EXER_DIR="$2"
else
  # find all .c files under submissions/
  mapfile -t SUBFILES < <(find submissions -type f -name "*.c" 2>/dev/null || true)
  EXER_DIR="" # not used globally
fi

if [ ${#SUBFILES[@]} -eq 0 ]; then
  echo "No submissions found under submissions/. Nothing to test." >&2
  exit 0
fi

ANY_FAIL=0
for file in "${SUBFILES[@]}"; do
  echo "== Testing submission: $file =="
  fname=$(basename "$file")
  # expect filename like dayN.c
  day=$(echo "$fname" | sed -E 's/^(day[0-9]+)\.c$/\1/')
  if [ -z "$day" ]; then
    echo "Cannot infer exercise id from filename $fname (expected dayNN.c). Skipping." >&2
    ANY_FAIL=1
    continue
  fi
  EXER="exercises/$day"
  if [ ! -d "$EXER" ]; then
    echo "Exercise directory $EXER not found for submission $file" >&2
    ANY_FAIL=1
    continue
  fi

  # compile
  gcc -std=c11 -O2 -Wall -Wextra "$file" -o /tmp/submission_exec || { echo "Compilation failed for $file"; ANY_FAIL=1; continue; }

  # run tests
  shopt -s nullglob
  inputs=("$EXER/tests/input"*.txt)
  if [ ${#inputs[@]} -eq 0 ]; then
    echo "No tests found in $EXER/tests. Marking as failed." >&2
    ANY_FAIL=1
    continue
  fi
  idx=1
  for inpath in "${inputs[@]}"; do
    outpath="$EXER/tests/output${inpath##*input}"
    # normalize names: input1.txt -> output1.txt
    outpath="${inpath/input/output}"
    if [ ! -f "$outpath" ]; then
      echo "Missing expected output file for $inpath (expected $outpath)" >&2
      ANY_FAIL=1
      continue
    fi

    /tmp/submission_exec < "$inpath" > /tmp/submission_out.txt || { echo "Runtime error on test $inpath"; ANY_FAIL=1; continue; }
    # trim trailing whitespace for comparison
    sed -E 's/[[:space:]]+$//' /tmp/submission_out.txt > /tmp/submission_out_trim.txt || true
    sed -E 's/[[:space:]]+$//' "$outpath" > /tmp/expected_out_trim.txt || true
    if ! diff -u /tmp/expected_out_trim.txt /tmp/submission_out_trim.txt >/dev/null; then
      echo "Test FAILED: $inpath" >&2
      echo "--- expected ---"; cat /tmp/expected_out_trim.txt; echo "--- got ---"; cat /tmp/submission_out_trim.txt
      ANY_FAIL=1
    else
      echo "Test passed: $inpath"
    fi
    idx=$((idx+1))
  done
done

if [ "$ANY_FAIL" -ne 0 ]; then
  echo "One or more tests failed." >&2
  exit 1
fi

echo "All tests passed." 
