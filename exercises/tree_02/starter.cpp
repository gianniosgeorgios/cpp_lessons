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

// Άθροισμα τιμών κόμβων
// Function name: sum_nodes
// Target complexity: O(N) χρόνος.
long long sum_nodes(node *t) {
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
    cout << sum_nodes(t) << '\n';
    return 0;
}
