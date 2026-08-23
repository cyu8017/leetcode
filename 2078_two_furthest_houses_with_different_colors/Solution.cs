// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

using System;

public class Solution {
    public int MaxDistance(int[] colors) {
        int n = colors.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[0]) ans = Math.Max(ans, i);
            if (colors[i] != colors[n - 1]) ans = Math.Max(ans, n - 1 - i);
        }
        return ans;
    }
}
