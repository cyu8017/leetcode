// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

class Solution {
    public int houseOfCards(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int k = 1; 3 * k - 1 <= n; k++) {
            int cost = 3 * k - 1;
            for (int j = n; j >= cost; j--) dp[j] += dp[j - cost];
        }
        return dp[n];
    }
}
