// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

using System;

public class Solution {
    public long SplitArray(int[] nums) {
        int n = nums.Length;
        long[] s = new long[n];
        bool[] f = new bool[n], g = new bool[n];
        for (int i = 0; i < n; i++) { f[i] = true; g[i] = true; }
        s[0] = nums[0];
        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + nums[i];
            f[i] = f[i - 1];
            if (nums[i] <= nums[i - 1]) f[i] = false;
        }
        for (int i = n - 2; i >= 0; i--) {
            g[i] = g[i + 1];
            if (nums[i] <= nums[i + 1]) g[i] = false;
        }
        const long inf = long.MaxValue / 4;
        long ans = inf;
        for (int i = 0; i < n - 1; i++) {
            if (f[i] && g[i + 1]) {
                long s1 = s[i], s2 = s[n - 1] - s[i];
                ans = Math.Min(ans, Math.Abs(s1 - s2));
            }
        }
        return ans < inf ? ans : -1;
    }
}
