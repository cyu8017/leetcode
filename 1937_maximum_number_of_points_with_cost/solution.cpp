// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxPoints(std::vector<std::vector<int>>& points) {
        int m = (int)points.size(), n = (int)points[0].size();
        std::vector<long long> dp(n);
        for (int c = 0; c < n; c++) dp[c] = points[0][c];
        for (int r = 1; r < m; r++) {
            std::vector<long long> left(n), right(n), ndp(n);
            left[0] = dp[0];
            for (int c = 1; c < n; c++) left[c] = std::max(left[c - 1] - 1, dp[c]);
            right[n - 1] = dp[n - 1];
            for (int c = n - 2; c >= 0; c--) right[c] = std::max(right[c + 1] - 1, dp[c]);
            for (int c = 0; c < n; c++) ndp[c] = points[r][c] + std::max(left[c], right[c]);
            dp.swap(ndp);
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};
