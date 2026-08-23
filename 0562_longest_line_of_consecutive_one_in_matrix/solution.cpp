// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestLine(std::vector<std::vector<int>>& mat) {
        if (mat.empty() || mat[0].empty()) {
            return 0;
        }

        int rows = static_cast<int>(mat.size());
        int cols = static_cast<int>(mat[0].size());
        std::vector<std::vector<std::vector<int>>> dp(
            rows, std::vector<std::vector<int>>(cols, std::vector<int>(4, 0)));
        int best = 0;

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (mat[r][c] == 0) {
                    continue;
                }
                dp[r][c][0] = (c > 0 ? dp[r][c - 1][0] : 0) + 1;
                dp[r][c][1] = (r > 0 ? dp[r - 1][c][1] : 0) + 1;
                dp[r][c][2] = (r > 0 && c > 0 ? dp[r - 1][c - 1][2] : 0) + 1;
                dp[r][c][3] = (r > 0 && c + 1 < cols ? dp[r - 1][c + 1][3] : 0) + 1;
                best = std::max(best, *std::max_element(dp[r][c].begin(), dp[r][c].end()));
            }
        }
        return best;
    }
};
