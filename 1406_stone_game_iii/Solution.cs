// LeetCode 1406 - Stone Game Iii
// https://leetcode.com/problems/stone-game-iii/

public class Solution {
    public string StoneGameIII(int[] stoneValue) {
        int n = stoneValue.Length;
        var dp = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            long take = 0; dp[i] = long.MinValue / 4;
            for (int j = i; j < System.Math.Min(i + 3, n); j++) {
                take += stoneValue[j];
                dp[i] = System.Math.Max(dp[i], take - dp[j + 1]);
            }
        }
        return dp[0] > 0 ? "Alice" : dp[0] < 0 ? "Bob" : "Tie";
    }
}
