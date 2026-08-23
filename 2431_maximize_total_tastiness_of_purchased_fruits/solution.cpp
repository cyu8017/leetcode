// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxTastiness(std::vector<int>& price, std::vector<int>& tastiness, int maxAmount, int maxCoupons) {
        int n = (int)price.size();
        std::vector<std::vector<int>> dp(maxAmount + 1, std::vector<int>(maxCoupons + 1, INT_MIN / 2));
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            int p = price[i], t = tastiness[i];
            for (int a = maxAmount; a >= 0; a--) {
                for (int c = maxCoupons; c >= 0; c--) {
                    if (dp[a][c] < 0) continue;
                    if (a + p <= maxAmount) {
                        dp[a + p][c] = std::max(dp[a + p][c], dp[a][c] + t);
                    }
                    if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount) {
                        dp[a + p / 2][c + 1] = std::max(dp[a + p / 2][c + 1], dp[a][c] + t);
                    }
                }
            }
        }
        int ans = 0;
        for (int a = 0; a <= maxAmount; a++) {
            for (int c = 0; c <= maxCoupons; c++) {
                ans = std::max(ans, dp[a][c]);
            }
        }
        return ans;
    }
};
