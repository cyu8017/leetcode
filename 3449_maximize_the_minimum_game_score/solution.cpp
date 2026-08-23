// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& points, int m) {
        auto ok = [&](long long mid) {
            long long need = 0;
            long long extra = 0;
            for (int p : points) {
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
        };
        long long lo = 0, hi = (long long)1e18;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
