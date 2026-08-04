// LeetCode 1406 - Stone Game Iii
// https://leetcode.com/problems/stone-game-iii/

class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        var dp = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            long take = 0; dp[i] = Long.MIN_VALUE / 4;
            for (int j = i; j < Math.min(i + 3, n); j++) {
                take += stoneValue[j];
                dp[i] = Math.max(dp[i], take - dp[j + 1]);
            }
        }
        return dp[0] > 0 ? "Alice" : dp[0] < 0 ? "Bob" : "Tie";
    }
}
