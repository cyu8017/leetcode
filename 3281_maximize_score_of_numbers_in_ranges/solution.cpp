// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    int maxPossibleScore(std::vector<int>& start, int d) {
        std::sort(start.begin(), start.end());
        int n = (int)start.size();
        auto ok = [&](int mid) {
            int64_t prev = start[0];
            for (int i = 1; i < n; i++) {
                int64_t need = prev + mid;
                int64_t cur = start[i];
                if (need > cur + d) return false;
                prev = need > cur ? need : cur;
            }
            return true;
        };
        int lo = 0, hi = start[n - 1] + d - start[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
