// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

using System;
using System.Linq;

public class Solution {
    public int MaxWidthOfVerticalArea(int[][] points) {
        var x = points.Select(p => p[0]).OrderBy(v => v).ToArray();
        int ans = 0;
        for (int i = 1; i < x.Length; i++) ans = Math.Max(ans, x[i] - x[i - 1]);
        return ans;
    }
}
