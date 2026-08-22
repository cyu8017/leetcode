// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

#include <stdbool.h>

static bool ok3449(int* points, int n, int m, long long mid) {
    long long need = 0, extra = 0;
    for (int i = 0; i < n; i++) {
        long long p = points[i];
        long long req = (mid + p - 1) / p;
        if (req > extra) {
            long long visits = req - extra;
            need += 2 * visits - 1;
            extra = visits - 1;
        } else {
            need += 1;
            extra = 0;
        }
        if (need > m) return false;
    }
    return need <= m;
}

long long maxScore(int* points, int pointsSize, int m) {
    long long lo = 0, hi = 1000000000000000000LL;
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        if (ok3449(points, pointsSize, m, mid)) lo = mid; else hi = mid - 1;
    }
    return lo;
}
