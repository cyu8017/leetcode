// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

#include <vector>

class Solution {
public:
    int minLargest(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size(), m = (int)nums2.size();
        const int inf = 1000000000;
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, inf));
        dp[0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (dp[i][j] == inf) continue;
                int prev = dp[i][j];
                if (i < n) {
                    int need = prev + 1;
                    if (nums1[i] == 0) {
                        if (need % 2 != 0) need++;
                    } else {
                        if (need % 2 == 0) need++;
                    }
                    if (need < dp[i + 1][j]) dp[i + 1][j] = need;
                }
                if (j < m) {
                    int need = prev + 1;
                    if (nums2[j] == 0) {
                        if (need % 2 != 0) need++;
                    } else {
                        if (need % 2 == 0) need++;
                    }
                    if (need < dp[i][j + 1]) dp[i][j + 1] = need;
                }
            }
        }
        return dp[n][m];
    }
};
