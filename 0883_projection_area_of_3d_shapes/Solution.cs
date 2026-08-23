// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

using System;

public class Solution {
    public int ProjectionArea(int[][] grid) {
        int n = grid.Length;
        int top = 0, front = 0, side = 0;
        for (int i = 0; i < n; i++) {
            int rowMax = 0, colMax = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) top++;
                rowMax = Math.Max(rowMax, grid[i][j]);
                colMax = Math.Max(colMax, grid[j][i]);
            }
            front += rowMax;
            side += colMax;
        }
        return top + front + side;
    }
}
