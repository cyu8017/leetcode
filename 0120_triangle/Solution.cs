// LeetCode 0120 - Triangle
// https://leetcode.com/problems/triangle/

using System.Collections.Generic;

public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        int[] dp = new int[triangle.Count + 1];
        for (int row = triangle.Count - 1; row >= 0; row--) {
            for (int col = 0; col <= row; col++) {
                dp[col] = triangle[row][col] + System.Math.Min(dp[col], dp[col + 1]);
            }
        }
        return dp[0];
    }
}