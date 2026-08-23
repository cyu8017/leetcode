// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

using System;

public class Solution {
    public int LongestArithmetic(int[] nums) {
        int n = nums.Length;
        var d = new int[n];
        for (int i = 1; i < n; i++) d[i] = nums[i] - nums[i - 1];
        var f = new int[n];
        var g = new int[n];
        Array.Fill(f, 2); Array.Fill(g, 2);
        f[0] = 1;
        g[n - 1] = 1;
        for (int i = 2; i < n; i++) {
            if (d[i] == d[i - 1]) f[i] = f[i - 1] + 1;
        }
        for (int i = n - 3; i >= 0; i--) {
            if (d[i + 1] == d[i + 2]) g[i] = g[i + 1] + 1;
        }
        int ans = 3;
        for (int i = 0; i < n; i++) {
            ans = Math.Max(ans, Math.Max(f[i], g[i]));
            if (i > 0) ans = Math.Max(ans, f[i - 1] + 1);
            if (i + 1 < n) ans = Math.Max(ans, g[i + 1] + 1);
            if (i > 0 && i < n - 1) {
                int diff = nums[i + 1] - nums[i - 1];
                if (diff % 2 == 0) {
                    diff /= 2;
                    int k = 3;
                    if (i > 1 && diff == d[i - 1]) k += f[i - 1] - 1;
                    if (i < n - 2 && diff == d[i + 2]) k += g[i + 1] - 1;
                    ans = Math.Max(ans, k);
                }
            }
        }
        return ans;
    }
}
