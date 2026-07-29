// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minSpaceWastedKResizing(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const long long INF = (long long)1e18;
        std::vector<std::vector<long long>> waste(n, std::vector<long long>(n));
        for (int i = 0; i < n; i++) {
            int mx = 0;
            long long total = 0;
            for (int j = i; j < n; j++) {
                mx = std::max(mx, nums[j]);
                total += nums[j];
                waste[i][j] = (long long)mx * (j - i + 1) - total;
            }
        }
        int segments = k + 1;
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(segments + 1, INF));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int s = 1; s <= std::min(segments, i); s++) {
                for (int p = s - 1; p < i; p++) {
                    dp[i][s] = std::min(dp[i][s], dp[p][s - 1] + waste[p][i - 1]);
                }
            }
        }
        long long ans = INF;
        for (int s = 1; s <= segments; s++) ans = std::min(ans, dp[n][s]);
        return (int)ans;
    }
};
