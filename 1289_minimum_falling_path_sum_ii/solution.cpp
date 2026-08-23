// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minFallingPathSum(std::vector<std::vector<int>>& grid) {
        std::vector<int> dp = grid[0];
        for (int r = 1; r < static_cast<int>(grid.size()); ++r) {
            int first = 0;
            for (int i = 1; i < static_cast<int>(dp.size()); ++i) {
                if (dp[i] < dp[first]) {
                    first = i;
                }
            }
            int secondValue = INT_MAX;
            for (int i = 0; i < static_cast<int>(dp.size()); ++i) {
                if (i != first) {
                    secondValue = std::min(secondValue, dp[i]);
                }
            }
            if (static_cast<int>(dp.size()) == 1) {
                secondValue = 0;
            }
            std::vector<int> nxt(dp.size());
            for (int i = 0; i < static_cast<int>(grid[r].size()); ++i) {
                nxt[i] = grid[r][i] + (i == first ? secondValue : dp[first]);
            }
            dp.swap(nxt);
        }
        return *std::min_element(dp.begin(), dp.end());
    }
};
