// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

using System.Collections.Generic;

public class Solution {
    public int NumSubmat(int[][] mat) {
        int ans = 0;
        int cols = mat[0].Length;
        int[] heights = new int[cols];
        foreach (var row in mat) {
            for (int j = 0; j < cols; j++) {
                heights[j] = row[j] == 0 ? 0 : heights[j] + 1;
            }
            var stack = new Stack<(int h, int count)>();
            int running = 0;
            foreach (int h in heights) {
                int count = 1;
                while (stack.Count > 0 && stack.Peek().h >= h) {
                    var (old, width) = stack.Pop();
                    running -= old * width;
                    count += width;
                }
                stack.Push((h, count));
                running += h * count;
                ans += running;
            }
        }
        return ans;
    }
}
