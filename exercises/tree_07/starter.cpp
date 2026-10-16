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

// Κόμβοι με ύψος ίσο με βάθος
// Function name: count_height_equals_depth
// Target complexity: O(N) χρόνος· υπολογίστε τα ύψη χωρίς να επανεξετάζετε κάθε υποδέντρο πολλές φορές.
int count_height_equals_depth(node *t) {
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
    cout << count_height_equals_depth(t) << '\n';
    return 0;
}
