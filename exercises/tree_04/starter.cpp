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

// Μέγιστη τιμή στο δέντρο
// Function name: max_value
// Target complexity: O(N) χρόνος.
int max_value(node *t) {
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
    cout << max_value(t) << '\n';
    return 0;
}
