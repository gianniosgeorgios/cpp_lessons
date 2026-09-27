#include <stdio.h>

int max_subarray_sum(int N, int a[]) {
    if (N <= 0) return 0;
    int current = a[0], best = a[0];
    for (int i = 1; i < N; i++) {
        current = (current + a[i] > a[i]) ? current + a[i] : a[i];
        if (current > best) best = current;
    }
    return best;
}

int main(void) {
    int a[] = {-2,1,-3,4,-1,2,1,-5,4};
    printf("%d\n", max_subarray_sum(9, a));
    return 0;
}
