// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

using System;

public class Solution {
    public int ClimbStairs(int n, int[] costs) {
        const int inf = (int)1e9;
        int[] f = new int[n + 1];
        Array.Fill(f, inf);
        f[0] = 0;
        for (int i = 1; i <= n; i++) {
            int x = costs[i - 1];
            for (int j = Math.Max(0, i - 3); j < i; j++) {
                f[i] = Math.Min(f[i], f[j] + x + (i - j) * (i - j));
            }
        }
        return f[n];
    }
}
