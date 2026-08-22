// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

#include <stdbool.h>

long long repairCars(int* ranks, int ranksSize, int cars) {
    int mn = ranks[0];
    for (int i = 0; i < ranksSize; i++) if (ranks[i] < mn) mn = ranks[i];
    long long lo = 1, hi = (long long)mn * cars * cars;
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        long long done = 0;
        bool ok = false;
        for (int i = 0; i < ranksSize; i++) {
            long long r = ranks[i];
            long long l2 = 0, h2 = cars;
            while (l2 < h2) {
                long long m2 = (l2 + h2 + 1) / 2;
                if (r * m2 * m2 <= mid) l2 = m2;
                else h2 = m2 - 1;
            }
            done += l2;
            if (done >= cars) { ok = true; break; }
        }
        if (ok || done >= cars) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
