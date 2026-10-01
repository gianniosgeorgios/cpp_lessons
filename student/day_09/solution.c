#include <stdio.h>

int pivot_index(int N, int a[]) {
    int total = 0, left = 0;
    for (int i = 0; i < N; i++) total += a[i];
    for (int i = 0; i < N; i++) {
        int right = total - left - a[i];
        if (left == right) return i;
        left += a[i];
    }
    return -1;
}

int main(void) {
    int a[] = {1, 7, 3, 6, 5, 6};
    printf("%d\n", pivot_index(6, a));
    return 0;
}
