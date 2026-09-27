#include <stdio.h>
#define TABLE_SIZE 10007

typedef struct { int key, index, used; } Entry;

static int hash_key(int key) {
    int h = key % TABLE_SIZE;
    return h < 0 ? h + TABLE_SIZE : h;
}

int two_sum(int N, int a[], int target, int result[2]) {
    Entry table[TABLE_SIZE] = {0};
    for (int i = 0; i < N; i++) {
        int needed = target - a[i];
        int h = hash_key(needed);
        while (table[h].used) {
            if (table[h].key == needed) {
                result[0] = table[h].index;
                result[1] = i;
                return 1;
            }
            h = (h + 1) % TABLE_SIZE;
        }
        h = hash_key(a[i]);
        while (table[h].used) h = (h + 1) % TABLE_SIZE;
        table[h].used = 1;
        table[h].key = a[i];
        table[h].index = i;
    }
    return 0;
}

int main(void) {
    int a[] = {2, 7, 11, 15}, result[2];
    if (two_sum(4, a, 9, result)) printf("%d,%d\n", result[0], result[1]);
    return 0;
}
