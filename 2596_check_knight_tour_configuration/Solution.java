// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

class Solution {
    public boolean checkValidGrid(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0) return false;
        int[][] pos = new int[n * n][2];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                pos[grid[i][j]] = new int[] {i, j};
        int[][] dirs = {
            {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
            {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
        };
        for (int v = 0; v + 1 < n * n; ++v) {
            int r = pos[v][0], c = pos[v][1];
            boolean ok = false;
            for (int[] d : dirs) {
                if (r + d[0] == pos[v + 1][0] && c + d[1] == pos[v + 1][1]) {
                    ok = true;
                    break;
                }
            }
            if (!ok) return false;
        }
        return true;
    }
}
