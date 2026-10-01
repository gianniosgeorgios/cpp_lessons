#include <iostream>
using namespace std;

int remove_duplicates(int N, int a[]) {
    if (N <= 0) return 0;

    int pos = 1;
    for (int i = 1; i < N; i++) {
        if (a[i] != a[pos - 1]) {
            a[pos] = a[i];
            pos++;
        }
    }
    return pos;
}

int main() {
    int a[] = {1, 1, 2, 2, 2, 3, 4, 4};
    int len = remove_duplicates(8, a);
    cout << len << '\n';
    for (int i = 0; i < len; i++) {
        cout << a[i] << (i == len - 1 ? '\n' : ' ');
    }
    return 0;
}
