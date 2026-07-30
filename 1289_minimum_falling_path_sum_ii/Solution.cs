// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

using System.Linq;

public class Solution {
    public int MinFallingPathSum(int[][] grid) {
        var dp = (int[])grid[0].Clone();
        for (int rowIndex = 1; rowIndex < grid.Length; rowIndex++) {
            int[] row = grid[rowIndex];
            int first = 0;
            for (int i = 1; i < dp.Length; i++) {
                if (dp[i] < dp[first]) first = i;
            }
            int secondValue = int.MaxValue;
            for (int i = 0; i < dp.Length; i++) {
                if (i != first) secondValue = System.Math.Min(secondValue, dp[i]);
            }
            if (dp.Length == 1) secondValue = 0;
            var next = new int[dp.Length];
            for (int i = 0; i < row.Length; i++) {
                next[i] = row[i] + (i == first ? secondValue : dp[first]);
            }
            dp = next;
        }
        return dp.Min();
    }
}
