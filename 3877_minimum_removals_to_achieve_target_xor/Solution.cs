// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

using System;

public class Solution {
    public int MinRemovals(int[] nums, int target) {
        int mx = 0;
        foreach (int x in nums) mx = Math.Max(mx, x);
        int m = 0;
        if (mx > 0) {
            uint u = (uint)mx;
            while (u != 0) { m++; u >>= 1; }
        }
        if ((1 << m) <= target) return -1;
        int n = nums.Length;
        int N = 1 << m;
        var f = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            f[i] = new int[N];
            Array.Fill(f[i], int.MinValue);
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            for (int j = 0; j < N; j++) {
                f[i][j] = f[i - 1][j];
                if (f[i - 1][j ^ x] != int.MinValue) {
                    f[i][j] = Math.Max(f[i][j], f[i - 1][j ^ x] + 1);
                }
            }
        }
        if (f[n][target] < 0) return -1;
        return n - f[n][target];
    }
}
