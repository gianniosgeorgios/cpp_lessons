#include <stdio.h>

void move_zeros(int N, int a[]) {
    int pos = 0;
    for (int i = 0; i < N; i++) {
        if (a[i] != 0) a[pos++] = a[i];
    }
    while (pos < N) a[pos++] = 0;
}

int main(void) {
    int a[] = {0, 1, 0, 3, 12};
    move_zeros(5, a);
    for (int i = 0; i < 5; i++) printf("%d%s", a[i], i == 4 ? "\n" : ",");
    return 0;
}
