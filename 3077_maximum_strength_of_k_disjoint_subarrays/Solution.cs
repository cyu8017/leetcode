// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

using System;

public class Solution {
    public long MaximumStrength(int[] nums, int k) {
        int n = nums.Length;
        const long Inf = long.MinValue / 2;
        long[][][] f = new long[n + 1][][];
        for (int i = 0; i <= n; i++) {
            f[i] = new long[k + 1][];
            for (int j = 0; j <= k; j++) {
                f[i][j] = new long[2];
                f[i][j][0] = Inf;
                f[i][j][1] = Inf;
            }
        }
        f[0][0][0] = 0;
        for (int i = 1; i <= n; i++) {
            long x = nums[i - 1];
            for (int j = 0; j <= k; j++) {
                long sign = (j & 1) != 0 ? 1 : -1;
                long val = sign * x * (k - j + 1);
                f[i][j][0] = Math.Max(f[i - 1][j][0], f[i - 1][j][1]);
                f[i][j][1] = Math.Max(f[i][j][1], f[i - 1][j][1] + val);
                if (j > 0) {
                    long t = Math.Max(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val;
                    f[i][j][1] = Math.Max(f[i][j][1], t);
                }
            }
        }
        return Math.Max(f[n][k][0], f[n][k][1]);
    }
}
