// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

#include <stdbool.h>

static bool ok(long long T, int* d, int* r) {
    long long w0 = T - T / r[0];
    long long w1 = T - T / r[1];
    return w0 + w1 >= (long long)d[0] + d[1];
}

long long minimumTime(int* d, int dSize, int* r, int rSize) {
    (void)dSize; (void)rSize;
    long long lo = 1, hi = 8000000000000000000LL;
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (ok(mid, d, r)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
