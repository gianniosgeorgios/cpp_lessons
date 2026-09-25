# ex01 — Sum of an array


Implement the function below (teacher provides `skeleton.h`) and keep no `main()` in your `task.c`.

Desired function (provided by teacher):

```
long long sum_array(int n, int *a);
```

Behavior: `sum_array` receives `n` and a pointer to an array `a` and returns the 64-bit sum of elements.

Requirements:
- Time complexity: O(N)
- Use 64-bit accumulation to avoid overflow for large totals.

Tests are in `exercises/ex01/tests/` and include `driverN.c`, `inputN.txt`, and `expectedN.txt`.
