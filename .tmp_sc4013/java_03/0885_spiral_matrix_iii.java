// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

import java.util.*;

class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        List<int[]> ans = new ArrayList<>();
        ans.add(new int[] {rStart, cStart});
        if (rows * cols == 1) return ans.toArray(new int[0][]);
        int r = rStart, c = cStart;
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int steps = 1;
        while (ans.size() < rows * cols) {
            for (int d = 0; d < 4; d++) {
                int dr = dirs[d][0], dc = dirs[d][1];
                for (int i = 0; i < steps; i++) {
                    r += dr;
                    c += dc;
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans.add(new int[] {r, c});
                        if (ans.size() == rows * cols) return ans.toArray(new int[0][]);
                    }
                }
                if (d % 2 == 1) steps++;
            }
        }
        return ans.toArray(new int[0][]);
    }
}
