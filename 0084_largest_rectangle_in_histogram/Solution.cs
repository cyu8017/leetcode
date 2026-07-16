// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

using System;
using System.Collections.Generic;

public class Solution {
    public int LargestRectangleArea(int[] heights) {
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
