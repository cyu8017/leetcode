// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

using System.Collections.Generic;

public class Solution {
    public int[][] SeePeople(int[][] heights) {
        int m = heights.Length, n = heights[0].Length;
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        for (int i = 0; i < m; i++) {
            var stack = new List<int>();
            for (int j = n - 1; j >= 0; j--) {
                int cnt = 0;
                while (stack.Count > 0 && heights[i][stack[stack.Count - 1]] < heights[i][j]) { stack.RemoveAt(stack.Count - 1); cnt++; }
                if (stack.Count > 0) cnt++;
                ans[i][j] += cnt;
                while (stack.Count > 0 && heights[i][stack[stack.Count - 1]] == heights[i][j]) stack.RemoveAt(stack.Count - 1);
                stack.Add(j);
            }
        }
        for (int j = 0; j < n; j++) {
            var stack = new List<int>();
            for (int i = m - 1; i >= 0; i--) {
                int cnt = 0;
                while (stack.Count > 0 && heights[stack[stack.Count - 1]][j] < heights[i][j]) { stack.RemoveAt(stack.Count - 1); cnt++; }
                if (stack.Count > 0) cnt++;
                ans[i][j] += cnt;
                while (stack.Count > 0 && heights[stack[stack.Count - 1]][j] == heights[i][j]) stack.RemoveAt(stack.Count - 1);
                stack.Add(i);
            }
        }
        return ans;
    }
}
