// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumTastiness(int* price, int priceSize, int k) {
    qsort(price, (size_t)priceSize, sizeof(int), cmp_int);
    int lo = 0, hi = price[priceSize - 1] - price[0];
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        int cnt = 1, last = price[0];
        int ok = 0;
        for (int i = 1; i < priceSize; i++) {
            if (price[i] - last >= mid) {
                cnt++;
                last = price[i];
                if (cnt >= k) { ok = 1; break; }
            }
        }
        if (ok) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
