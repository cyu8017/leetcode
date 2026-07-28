// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.length, n = grid[0].length, original = grid[row][col];
        Set<Long> component = new HashSet<>();
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{row, col});
        component.add(key(row, col));
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                long k = key(nr, nc);
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original && component.add(k)) {
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        List<long[]> border = new ArrayList<>();
        for (long k : component) {
            int r = (int) (k >> 32), c = (int) k;
            boolean isBorder = false;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || !component.contains(key(nr, nc))) {
                    isBorder = true;
                    break;
                }
            }
            if (isBorder) border.add(new long[]{r, c});
        }
        for (long[] cell : border) grid[(int) cell[0]][(int) cell[1]] = color;
        return grid;
    }

    private long key(int r, int c) {
        return (((long) r) << 32) | (c & 0xffffffffL);
    }
}
