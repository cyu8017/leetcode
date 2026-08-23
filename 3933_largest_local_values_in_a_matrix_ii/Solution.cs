// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int CountLocalMaximums(int[][] matrix) {
        int rows = matrix.Length, cols = matrix[0].Length;
        var positions = new List<(int row, int col)>[201];
        for (int i = 0; i < 201; i++) positions[i] = new List<(int, int)>();
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int value = matrix[row][col];
                if (value > 0) positions[value].Add((row, col));
            }
        }
        int answer = 0;
        for (int value = 1; value <= 200; value++) {
            if (positions[value].Count == 0) continue;
            int[][] prefix = new int[rows + 1][];
            for (int i = 0; i <= rows; i++) prefix[i] = new int[cols + 1];
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int add = matrix[row][col] > value ? 1 : 0;
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            foreach (var (row, col) in positions[value]) {
                int top = Math.Max(0, row - value), bottom = Math.Min(rows - 1, row + value);
                int left = Math.Max(0, col - value), right = Math.Min(cols - 1, col + value);
                int greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
                foreach (int dr in new[] { -value, value }) {
                    foreach (int dc in new[] { -value, value }) {
                        int rr = row + dr, cc = col + dc;
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--;
                    }
                }
                if (greater == 0) answer++;
            }
        }
        return answer;
    }
}
