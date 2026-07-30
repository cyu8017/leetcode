// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

public class Solution {
    public int NumWays(int steps, int arrLen) {
        const int mod = 1_000_000_007;
        int width = System.Math.Min(arrLen, steps / 2 + 1);
        var dp = new int[width];
        dp[0] = 1;
        for (int s = 0; s < steps; s++) {
            var next = new int[width];
            for (int i = 0; i < width; i++) {
                next[i] = dp[i];
                if (i > 0) next[i] = (next[i] + dp[i - 1]) % mod;
                if (i + 1 < width) next[i] = (next[i] + dp[i + 1]) % mod;
            }
            dp = next;
        }
        return dp[0];
    }
}
