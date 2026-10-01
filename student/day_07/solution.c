#include <stdio.h>

int is_sorted(int N, int a[]) {
    for (int i = 1; i < N; i++) {
        if (a[i] < a[i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main(void) {
    int a[] = {2, 4, 7, 9, 11};
    printf("%d\n", is_sorted(5, a));
    return 0;
}
