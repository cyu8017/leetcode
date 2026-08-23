// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

class Solution {
    public int rearrangeSticks(int n, int k) {
        int mod = 1_000_000_007;
        if (k == 0 || k > n) {
            return 0;
        }

        int[][] dp = new int[n + 1][n + 1];
        dp[1][1] = 1;
        for (int sticks = 2; sticks <= n; sticks++) {
            dp[sticks][1] = (int) ((long) (sticks - 1) * dp[sticks - 1][1] % mod);
            for (int visible = 2; visible <= sticks; visible++) {
                dp[sticks][visible] = (int) (
                    (dp[sticks - 1][visible - 1] + (long) (sticks - 1) * dp[sticks - 1][visible]) % mod
                );
            }
        }

        return dp[n][k];
    }
}
