// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

#include <stdbool.h>

static bool possible(int* bloomDay, int n, int m, int k, int day) {
    int bouquets = 0, run = 0;
    for (int i = 0; i < n; i++) {
        run = bloomDay[i] <= day ? run + 1 : 0;
        if (run == k) { bouquets++; run = 0; }
    }
    return bouquets >= m;
}

int minDays(int* bloomDay, int bloomDaySize, int m, int k) {
    if ((long long)m * k > bloomDaySize) return -1;
    int lo = bloomDay[0], hi = bloomDay[0];
    for (int i = 1; i < bloomDaySize; i++) {
        if (bloomDay[i] < lo) lo = bloomDay[i];
        if (bloomDay[i] > hi) hi = bloomDay[i];
    }
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (possible(bloomDay, bloomDaySize, m, k, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
