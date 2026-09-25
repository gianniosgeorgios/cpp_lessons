// Template for implementing the required function only.
// Copy to submissions/<exercise-id>/task.c or student/<exercise-id>.c
#include "../../exercises/ex01/skeleton.h"

/* Implement the function declared in skeleton.h */
long long sum_array(int n, int *a){
    long long sum = 0;
    for(int i=0;i<n;i++) sum += a[i];
    return sum;
}
