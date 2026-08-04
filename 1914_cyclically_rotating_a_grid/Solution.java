// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

import java.util.*;

class Solution {
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int layers = Math.min(m, n) / 2;
        for (int layer = 0; layer < layers; layer++) {
            List<Integer> vals = new ArrayList<>();
            for (int c = layer; c < n - layer; c++) vals.add(grid[layer][c]);
            for (int r = layer + 1; r < m - layer; r++) vals.add(grid[r][n - layer - 1]);
            if (m - 2 * layer > 1) {
                for (int c = n - layer - 2; c >= layer; c--) vals.add(grid[m - layer - 1][c]);
            }
            if (n - 2 * layer > 1) {
                for (int r = m - layer - 2; r > layer; r--) vals.add(grid[r][layer]);
            }
            int shift = k % vals.size();
            List<Integer> rotated = new ArrayList<>();
            rotated.addAll(vals.subList(shift, vals.size()));
            rotated.addAll(vals.subList(0, shift));
            int idx = 0;
            for (int c = layer; c < n - layer; c++) grid[layer][c] = rotated.get(idx++);
            for (int r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = rotated.get(idx++);
            if (m - 2 * layer > 1) {
                for (int c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = rotated.get(idx++);
            }
            if (n - 2 * layer > 1) {
                for (int r = m - layer - 2; r > layer; r--) grid[r][layer] = rotated.get(idx++);
            }
        }
        return grid;
    }
}
