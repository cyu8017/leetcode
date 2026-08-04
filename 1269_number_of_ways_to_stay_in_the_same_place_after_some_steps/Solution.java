// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    public int numWays(int steps, int arrLen) {
        int mod = 1_000_000_007;
        int width = Math.min(arrLen, steps / 2 + 1);
        int[] dp = new int[width];
        dp[0] = 1;
        for (int s = 0; s < steps; s++) {
            int[] next = new int[width];
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
