// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

#include <stdbool.h>

static bool ok(long long machines, int n, int budget, int** composition, int compositionSize, int* stock, int* cost) {
    for (int t = 0; t < compositionSize; t++) {
        long long spend = 0;
        for (int i = 0; i < n; i++) {
            long long need = machines * composition[t][i] - stock[i];
            if (need > 0) spend += need * cost[i];
        }
        if (spend <= budget) return true;
    }
    return false;
}

int maxNumberOfAlloys(int n, int k, int budget, int** composition, int compositionSize, int* compositionColSize, int* stock, int stockSize, int* cost, int costSize) {
    (void)k; (void)compositionColSize; (void)stockSize; (void)costSize;
    long long lo = 0, hi = 1000000000LL, ans = 0;
    while (lo <= hi) {
        long long mid = (lo + hi) / 2;
        if (ok(mid, n, budget, composition, compositionSize, stock, cost)) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return (int)ans;
}
