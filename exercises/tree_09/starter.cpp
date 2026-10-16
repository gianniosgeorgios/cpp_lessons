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

// Μεγαλύτερο γνήσια φθίνον μονοπάτι
// Function name: longest_decreasing_path
// Target complexity: O(N) χρόνος.
int longest_decreasing_path(node *t) {
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
    cout << longest_decreasing_path(t) << '\n';
    return 0;
}
