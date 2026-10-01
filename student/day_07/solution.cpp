#include <iostream>
using namespace std;

int is_sorted(int N, int a[]) {
    for (int i = 1; i < N; i++) {
        if (a[i] < a[i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int a[] = {2, 4, 7, 9, 11};
    cout << is_sorted(5, a) << '\n';
    return 0;
}
