// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

#include <stdbool.h>

static int gcd3116(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}
static int lcm3116(int a, int b) {
    return a / gcd3116(a, b) * b;
}
static int popcount3116(unsigned x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}
static bool ok3116(int* coins, int n, long long mx, int k) {
    long long cnt = 0;
    for (int i = 1; i < (1 << n); i++) {
        long long v = 1;
        for (int j = 0; j < n; j++) {
            if ((i >> j) & 1) {
                v = lcm3116((int)v, coins[j]);
                if (v > mx) break;
            }
        }
        int m = popcount3116((unsigned)i);
        if (m % 2 == 1) cnt += mx / v;
        else cnt -= mx / v;
    }
    return cnt >= k;
}

long long findKthSmallest(int* coins, int coinsSize, int k) {
    long long lo = 1, hi = 100000000000LL; /* 1e11 */
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (ok3116(coins, coinsSize, mid, k)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
