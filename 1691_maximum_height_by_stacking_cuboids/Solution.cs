// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

using System;

public class Solution {
    public int MaxHeight(int[][] cuboids) {
        foreach (var c in cuboids) Array.Sort(c);
        Array.Sort(cuboids, (a, b) => {
            int cmp = a[0].CompareTo(b[0]);
            if (cmp != 0) return cmp;
            cmp = a[1].CompareTo(b[1]);
            if (cmp != 0) return cmp;
            return a[2].CompareTo(b[2]);
        });
        int n = cuboids.Length;
        int[] dp = new int[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = cuboids[i][2];
            for (int j = 0; j < i; j++) {
                if (cuboids[j][0] <= cuboids[i][0] &&
                    cuboids[j][1] <= cuboids[i][1] &&
                    cuboids[j][2] <= cuboids[i][2]) {
                    dp[i] = Math.Max(dp[i], dp[j] + cuboids[i][2]);
                }
            }
            ans = Math.Max(ans, dp[i]);
        }
        return ans;
    }
}
