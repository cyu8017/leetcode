// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minFallingPathSum(std::vector<std::vector<int>>& matrix) {
        std::vector<int> dp = matrix[0];
        for (int r = 1; r < (int)matrix.size(); r++) {
            std::vector<int> ndp(dp.size());
            for (int c = 0; c < (int)dp.size(); c++) {
                int best = dp[c];
                if (c) best = std::min(best, dp[c - 1]);
                if (c + 1 < (int)dp.size()) best = std::min(best, dp[c + 1]);
                ndp[c] = matrix[r][c] + best;
            }
            dp.swap(ndp);
        }
        return *std::min_element(dp.begin(), dp.end());
    }
};
