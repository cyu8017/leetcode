// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

using System;

public class Solution {
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        const long inf = long.MinValue / 4;
        long[][] f = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            f[i] = new long[4];
            for (int j = 0; j < 4; j++) f[i][j] = inf;
        }
        f[0][0] = 0;
        long ans = inf;
        for (int i = 1; i <= n; i++) {
            long x = nums[i - 1];
            f[i][0] = Math.Max(f[i - 1][0], 0L) + x;
            f[i][1] = Math.Max(Math.Max(f[i - 1][0], f[i - 1][1]), 0L) + x * k;
            f[i][2] = Math.Max(Math.Max(f[i - 1][0], f[i - 1][2]), 0L) + x / k;
            f[i][3] = Math.Max(Math.Max(f[i - 1][1], f[i - 1][2]), f[i - 1][3]) + x;
            ans = Math.Max(ans, Math.Max(Math.Max(f[i][0], f[i][1]), Math.Max(f[i][2], f[i][3])));
        }
        return ans;
    }
}
