// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution {
    public int sumOfPower(int[] nums, int k) {
        final int MOD = 1_000_000_007;
        int n = nums.length;
        int[][] f = new int[n + 1][k + 1];
        f[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                f[i][j] = (int) ((f[i - 1][j] * 2L) % MOD);
                if (j >= nums[i - 1])
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD;
            }
        }
        return f[n][k];
    }
}
