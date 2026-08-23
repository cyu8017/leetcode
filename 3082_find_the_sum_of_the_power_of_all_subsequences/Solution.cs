// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

public class Solution {
    public int SumOfPower(int[] nums, int k) {
        const int Mod = 1000000007;
        int n = nums.Length;
        int[][] f = new int[n + 1][];
        for (int i = 0; i <= n; i++) f[i] = new int[k + 1];
        f[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                f[i][j] = (int)((f[i - 1][j] * 2L) % Mod);
                if (j >= nums[i - 1])
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % Mod;
            }
        }
        return f[n][k];
    }
}
