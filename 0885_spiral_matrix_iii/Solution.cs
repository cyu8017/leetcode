// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

using System.Collections.Generic;

public class Solution {
    public int[][] SpiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        var ans = new List<int[]> { new[] { rStart, cStart } };
        if (rows * cols == 1) return ans.ToArray();
        int r = rStart, c = cStart;
        int[][] dirs = new[] { new[] { 0, 1 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { -1, 0 } };
        int steps = 1;
        while (ans.Count < rows * cols) {
            for (int d = 0; d < 4; d++) {
                int dr = dirs[d][0], dc = dirs[d][1];
                for (int i = 0; i < steps; i++) {
                    r += dr;
                    c += dc;
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans.Add(new[] { r, c });
                        if (ans.Count == rows * cols) return ans.ToArray();
                    }
                }
                if (d % 2 == 1) steps++;
            }
        }
        return ans.ToArray();
    }
}
