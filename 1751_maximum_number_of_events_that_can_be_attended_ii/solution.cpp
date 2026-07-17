// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxValue(std::vector<std::vector<int>>& events, int k) {
        std::sort(events.begin(), events.end());
        int n = static_cast<int>(events.size());
        std::vector<int> starts(n);
        for (int i = 0; i < n; i++) {
            starts[i] = events[i][0];
        }

        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; i--) {
            int j = static_cast<int>(std::upper_bound(starts.begin(), starts.end(), events[i][1]) - starts.begin());
            for (int remain = 1; remain <= k; remain++) {
                dp[remain][i] = std::max(dp[remain][i + 1], events[i][2] + dp[remain - 1][j]);
            }
        }
        return dp[k][0];
    }
};
