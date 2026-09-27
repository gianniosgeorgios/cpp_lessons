#include <stdio.h>

int majority_element(int N, int a[]) {
    int candidate = 0, count = 0;
    for (int i = 0; i < N; i++) {
        if (count == 0) candidate = a[i];
        count += (a[i] == candidate) ? 1 : -1;
    }
    return candidate;
}

int main(void) {
    int a[] = {2,2,1,1,1,2,2};
    printf("%d\n", majority_element(7, a));
    return 0;
}
