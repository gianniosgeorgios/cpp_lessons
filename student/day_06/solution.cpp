#include <iostream>
#include <climits>
using namespace std;

int second_largest(int N, int a[]) {
    int largest = INT_MIN;
    int second = INT_MIN;

    for (int i = 0; i < N; i++) {
        if (a[i] > largest) {
            second = largest;
            largest = a[i];
        } else if (a[i] > second && a[i] != largest) {
            second = a[i];
        }
    }

    return second;
}

int main() {
    int a[] = {4, 9, 2, 11, 7};
    cout << second_largest(5, a) << '\n';
    return 0;
}
