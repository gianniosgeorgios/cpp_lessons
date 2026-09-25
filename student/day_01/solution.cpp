#include <iostream>
#include <vector>
using namespace std;

// Student function: find the maximum value in an array in O(N) time.
int find_max(const vector<int>& arr) {
    if (arr.empty()) {
        return 0;
    }

    int max_value = arr[0];
    for (int i = 1; i < static_cast<int>(arr.size()); ++i) {
        if (arr[i] > max_value) {
            max_value = arr[i];
        }
    }
    return max_value;
}

int main() {
    vector<int> sample = {3, 8, 1, 9, 4, 12, 5, 7};

    cout << "Example array: 3 8 1 9 4 12 5 7\n";
    cout << "Maximum value = " << find_max(sample) << '\n';

    return 0;
}
