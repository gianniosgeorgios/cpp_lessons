#include <stdio.h>
#include <limits.h>

int main(void) {
    int n;
    if (scanf("%d", &n)!=1) return 0;
    long long best = LLONG_MIN, cur = 0;
    for (int i=0;i<n;i++){
        int x; scanf("%d", &x);
        if (i==0) { cur = x; best = x; }
        else { cur = (cur>0?cur+x:x); if (cur>best) best=cur; }
    }
    printf("%lld\n", best);
    return 0;
}
