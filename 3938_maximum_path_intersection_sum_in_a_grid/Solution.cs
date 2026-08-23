// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

using System;

public class Solution {
    public int MaxPathSum(int[][] grid) {
        int rows = grid.Length, cols = grid[0].Length;
        int answer = int.MinValue;
        void CheckLine(int length, Func<int, int> value) {
            int bestEnding = value(0) + value(1);
            if (bestEnding > answer) answer = bestEnding;
            for (int i = 2; i < length; i++) {
                if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i);
                else bestEnding += value(i);
                if (bestEnding > answer) answer = bestEnding;
            }
        }
        for (int row = 0; row < rows; row++) {
            int r = row;
            CheckLine(cols, col => grid[r][col]);
        }
        for (int col = 0; col < cols; col++) {
            int c = col;
            CheckLine(rows, row => grid[row][c]);
        }
        for (int row = 1; row + 1 < rows; row++) {
            for (int col = 1; col + 1 < cols; col++) {
                if (grid[row][col] > answer) answer = grid[row][col];
            }
        }
        return answer;
    }
}
