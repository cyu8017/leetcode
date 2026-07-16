// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.Length == 0) {
            return 0;
        }

        int cols = matrix[0].Length;
        int[] heights = new int[cols];
        int maxArea = 0;

        foreach (char[] row in matrix) {
            for (int j = 0; j < cols; j++) {
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            }
            maxArea = Math.Max(maxArea, LargestHistogram(heights));
        }

        return maxArea;
    }

    private int LargestHistogram(int[] heights) {
        var stack = new Stack<int>();
        int maxArea = 0;
        int n = heights.Length;

        for (int i = 0; i <= n; i++) {
            int height = i == n ? 0 : heights[i];
            while (stack.Count > 0 && heights[stack.Peek()] > height) {
                int h = heights[stack.Pop()];
                int width = stack.Count == 0 ? i : i - stack.Peek() - 1;
                maxArea = Math.Max(maxArea, h * width);
            }
            stack.Push(i);
        }

        return maxArea;
    }
}
