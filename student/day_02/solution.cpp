#include <iostream>
using namespace std;

// Student function: find the minimum value in an array in O(N) time.
int find_min(int N, int a[]) {
    if (N <= 0) {
        return 0;
    }

    int min_value = a[0];
    for (int i = 1; i < N; ++i) {
        if (a[i] < min_value) {
            min_value = a[i];
        }
    }
    return min_value;
}

int main() {
    int sample[] = {8, 3, 12, 9, 4, 7, 1, 5};
    int N = 8;

    cout << find_min(N, sample) << '\n';

    return 0;
}
