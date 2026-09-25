// Student implementation for ex01: implement the function declared in skeleton.h
#include "../exercises/ex01/skeleton.h"

long long sum_array(int n, int *a){
    long long sum = 0;
    for(int i=0;i<n;i++) sum += a[i];
    return sum;
}
