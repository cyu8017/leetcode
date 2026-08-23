// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

#include <vector>

class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k - 1 + maxPts) {
            return 1.0;
        }
        std::vector<double> dp(n + 1, 0.0);
        dp[0] = 1.0;
        double window = 1.0, ans = 0.0;
        for (int i = 1; i <= n; ++i) {
            dp[i] = window / maxPts;
            if (i < k) {
                window += dp[i];
            } else {
                ans += dp[i];
            }
            if (i - maxPts >= 0 && i - maxPts < k) {
                window -= dp[i - maxPts];
            }
        }
        return ans;
    }
};
