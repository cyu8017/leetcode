// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] RotateGrid(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        int layers = Math.Min(m, n) / 2;
        for (int layer = 0; layer < layers; layer++) {
            var vals = new List<int>();
            for (int c = layer; c < n - layer; c++) vals.Add(grid[layer][c]);
            for (int r = layer + 1; r < m - layer; r++) vals.Add(grid[r][n - layer - 1]);
            if (m - 2 * layer > 1)
                for (int c = n - layer - 2; c >= layer; c--) vals.Add(grid[m - layer - 1][c]);
            if (n - 2 * layer > 1)
                for (int r = m - layer - 2; r > layer; r--) vals.Add(grid[r][layer]);
            int shift = k % vals.Count;
            var rotated = new List<int>();
            for (int i = 0; i < vals.Count; i++) rotated.Add(vals[(i + shift) % vals.Count]);
            int idx = 0;
            for (int c = layer; c < n - layer; c++) grid[layer][c] = rotated[idx++];
            for (int r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = rotated[idx++];
            if (m - 2 * layer > 1)
                for (int c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = rotated[idx++];
            if (n - 2 * layer > 1)
                for (int r = m - layer - 2; r > layer; r--) grid[r][layer] = rotated[idx++];
        }
        return grid;
    }
}