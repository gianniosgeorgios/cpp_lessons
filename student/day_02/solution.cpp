#include <iostream>
#include <vector>
using namespace std;

// Student function: find the minimum value in an array in O(N) time.
int find_min(const vector<int>& arr) {
    if (arr.empty()) {
        return 0;
    }

    int min_value = arr[0];
    for (int i = 1; i < static_cast<int>(arr.size()); ++i) {
        if (arr[i] < min_value) {
            min_value = arr[i];
        }
    }
    return min_value;
}

int main() {
    vector<int> sample = {8, 3, 12, 9, 4, 7, 1, 5};

    cout << "Example array: 8 3 12 9 4 7 1 5\n";
    cout << "Minimum value = " << find_min(sample) << '\n';

    return 0;
}
