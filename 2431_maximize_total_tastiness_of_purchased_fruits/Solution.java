// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

class Solution {
    public int maxTastiness(int[] price, int[] tastiness, int maxAmount, int maxCoupons) {
        int n = price.length;
        int[][] dp = new int[maxAmount + 1][];
        for (int a = 0; a <= maxAmount; a++) {
            dp[a] = new int[maxCoupons + 1];
            for (int c = 0; c <= maxCoupons; c++) dp[a][c] = Integer.MIN_VALUE / 2;
        }
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            int p = price[i], t = tastiness[i];
            for (int a = maxAmount; a >= 0; a--) {
                for (int c = maxCoupons; c >= 0; c--) {
                    if (dp[a][c] < 0) continue;
                    if (a + p <= maxAmount)
                        dp[a + p][c] = Math.max(dp[a + p][c], dp[a][c] + t);
                    if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount)
                        dp[a + p / 2][c + 1] = Math.max(dp[a + p / 2][c + 1], dp[a][c] + t);
                }
            }
        }
        int ans = 0;
        for (int a = 0; a <= maxAmount; a++)
            for (int c = 0; c <= maxCoupons; c++)
                ans = Math.max(ans, dp[a][c]);
        return ans;
    }
}
