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

// Μακρύτερο μονοπάτι από τη ρίζα χωρίς ίσους διαδοχικούς αριθμούς
// Function name: longest_path_no_equal_adjacent
// Target complexity: O(N) χρόνος.
int longest_path_no_equal_adjacent(node *t) {
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
    cout << longest_path_no_equal_adjacent(t) << '\n';
    return 0;
}
