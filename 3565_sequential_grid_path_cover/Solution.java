// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

import java.util.ArrayList;
import java.util.List;

class Solution {
    int m, n;
    long st;
    List<List<Integer>> path;
    int[] dirs = {-1, 0, 1, 0, -1};
    int[][] grid;

    int f(int i, int j) { return i * n + j; }

    boolean dfs(int i, int j, int v) {
        List<Integer> cell = new ArrayList<>();
        cell.add(i); cell.add(j);
        path.add(cell);
        if (path.size() == m * n) return true;
        int idx = f(i, j);
        st |= 1L << idx;
        if (grid[i][j] == v) v++;
        for (int t = 0; t < 4; t++) {
            int x = i + dirs[t], y = j + dirs[t + 1];
            if (0 <= x && x < m && 0 <= y && y < n) {
                int idx2 = f(x, y);
                if (((st >> idx2) & 1L) == 0 && (grid[x][y] == 0 || grid[x][y] == v)) {
                    if (dfs(x, y, v)) return true;
                }
            }
        }
        path.remove(path.size() - 1);
        st ^= 1L << idx;
        return false;
    }

    public List<List<Integer>> findPath(int[][] grid, int k) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        st = 0;
        path = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 || grid[i][j] == 1) {
                    if (dfs(i, j, 1)) return path;
                    path.clear();
                    st = 0;
                }
            }
        }
        return new ArrayList<>();
    }
}
