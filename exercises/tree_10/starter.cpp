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

// Διάμετρος δυαδικού δέντρου
// Function name: tree_diameter
// Target complexity: O(N) χρόνος: σε κάθε κόμβο υπολογίστε μαζί το ύψος και την καλύτερη διάμετρο.
int tree_diameter(node *t) {
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
    cout << tree_diameter(t) << '\n';
    return 0;
}
