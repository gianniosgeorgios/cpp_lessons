#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

struct node {
    int data;
    node *left;
    node *right;
    node(int value) : data(value), left(nullptr), right(nullptr) {}
};

// Άθροισμα κόμβων σε επίπεδο k
// Function name: sum_level
// Target complexity: O(N) χρόνος στη χειρότερη περίπτωση.
long long sum_level(node *t, int k) {
    // TODO: υλοποίησε τη συνάρτηση.
    return 0;
}

int main() {
    // Παράδειγμα:      8
    //                /   \
    //               3    10
    node *t = new node(8);
    t->left = new node(3);
    t->right = new node(10);
    cout << sum_level(t, 2) << '\n';
    return 0;
}
