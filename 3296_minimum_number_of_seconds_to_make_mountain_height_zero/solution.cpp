// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, std::vector<int>& workerTimes) {
        auto ok = [&](long long t) {
            long long total = 0;
            for (int w : workerTimes) {
                long long lo = 0, hi = mountainHeight;
                while (lo < hi) {
                    long long mid = (lo + hi + 1) / 2;
                    if ((long long)w * mid * (mid + 1) / 2 <= t) lo = mid;
                    else hi = mid - 1;
                }
                total += lo;
                if (total >= mountainHeight) return true;
            }
            return total >= mountainHeight;
        };
        long long lo = 0, hi = (long long)1e18;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
