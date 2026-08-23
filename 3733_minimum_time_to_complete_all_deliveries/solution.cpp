// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

#include <vector>

class Solution {
public:
    long long minimumTime(std::vector<int>& d, std::vector<int>& r) {
        auto ok = [&](long long T) {
            long long w0 = T - T / r[0];
            long long w1 = T - T / r[1];
            return w0 + w1 >= (long long)d[0] + d[1];
        };
        long long lo = 1, hi = (long long)8e18;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
