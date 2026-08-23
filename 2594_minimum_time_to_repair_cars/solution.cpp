// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long repairCars(std::vector<int>& ranks, int cars) {
        auto ok = [&](long long t) {
            long long done = 0;
            for (int r : ranks) {
                long long lo = 0, hi = cars;
                while (lo < hi) {
                    long long mid = (lo + hi + 1) / 2;
                    if ((long long)r * mid * mid <= t) lo = mid;
                    else hi = mid - 1;
                }
                done += lo;
                if (done >= cars) return true;
            }
            return done >= cars;
        };
        int mn = *std::min_element(ranks.begin(), ranks.end());
        long long lo = 1, hi = (long long)mn * cars * cars;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
