#include <iostream>
using namespace std;

// Student function: find the maximum value in an array in O(N) time.
int find_max(int N, int a[]) {
    if (N <= 0) {
        return 0;
    }

    int max_value = a[0];
    for (int i = 1; i < N; ++i) {
        if (a[i] > max_value) {
            max_value = a[i];
        }
    }
    return max_value;
}

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
    int sample[] = {3, 8, 1, 9, 4, 12, 5, 7};
    int N = 8;

    cout << "Example array: 3 8 1 9 4 12 5 7\n";
    cout << "Maximum value = " << find_max(N, sample) << '\n';
    cout << "Minimum value = " << find_min(N, sample) << '\n';

    return 0;
}
