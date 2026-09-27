#include <stdio.h>

int max_window_sum(int N, int a[], int k) {
    if (k <= 0 || k > N) return 0;
    int window = 0;
    for (int i = 0; i < k; i++) window += a[i];
    int best = window;
    for (int i = k; i < N; i++) {
        window += a[i] - a[i - k];
        if (window > best) best = window;
    }
    return best;
}

int main(void) {
    int a[] = {2,1,5,1,3,2};
    printf("%d\n", max_window_sum(6, a, 3));
    return 0;
}
