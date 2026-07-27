// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> numMovesStonesII(std::vector<int>& stones) {
        std::sort(stones.begin(), stones.end());
        int n = static_cast<int>(stones.size());
        int maxMoves = std::max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2);
        int minMoves = maxMoves;
        int i = 0;
        for (int j = 0; j < n; ++j) {
            while (stones[j] - stones[i] + 1 > n) ++i;
            int inside = j - i + 1;
            if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1) {
                minMoves = std::min(minMoves, 2);
            } else {
                minMoves = std::min(minMoves, n - inside);
            }
        }
        return {minMoves, maxMoves};
    }
};

