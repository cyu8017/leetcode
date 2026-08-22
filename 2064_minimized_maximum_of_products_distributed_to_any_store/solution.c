// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

#include <stdbool.h>

static bool can2064(int n, int* quantities, int qSize, int x) {
    int need = 0;
    for (int i = 0; i < qSize; i++) {
        need += (quantities[i] + x - 1) / x;
        if (need > n) return false;
    }
    return true;
}

int minimizedMaximum(int n, int* quantities, int quantitiesSize) {
    int lo = 1, hi = 0;
    for (int i = 0; i < quantitiesSize; i++) if (quantities[i] > hi) hi = quantities[i];
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (can2064(n, quantities, quantitiesSize, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
