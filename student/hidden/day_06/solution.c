#include <stdio.h>

int max_profit(int N, int prices[]) {
    if (N <= 1) return 0;
    int min_price = prices[0], best = 0;
    for (int i = 1; i < N; i++) {
        if (prices[i] < min_price) min_price = prices[i];
        else if (prices[i] - min_price > best) best = prices[i] - min_price;
    }
    return best;
}

int main(void) {
    int prices[] = {7, 1, 5, 3, 6, 4};
    printf("%d\n", max_profit(6, prices));
    return 0;
}
