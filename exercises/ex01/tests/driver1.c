// driver1.c — reads input1.txt, calls sum_array, prints result
#include <stdio.h>
#include "skeleton.h"

int main(void){
    int n;
    if(scanf("%d", &n)!=1) return 0;
    int *a = (int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++) scanf("%d", &a[i]);
    long long res = sum_array(n, a);
    printf("%lld\n", res);
    free(a);
    return 0;
}
