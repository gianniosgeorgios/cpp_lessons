#include <iostream>
using namespace std;

// Student function: calculate the sum of elements in an array in O(N) time.
int sum_array(int N, int a[]) {
    int total = 0;
    for (int i = 0; i < N; ++i) {
        total += a[i];
    }
    return total;
}

int main() {
    int sample[] = {1, 2, 3, 4, 5};
    int N = 5;

    cout << sum_array(N, sample) << '
';

    return 0;
}
