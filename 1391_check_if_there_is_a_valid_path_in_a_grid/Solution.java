// LeetCode 1391 - Check If There Is A Valid Path In A Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

import java.util.*;

class Solution {
    public boolean hasValidPath(int[][] grid) {
        int[][][] dirs = {
            {},
            {{0, -1}, {0, 1}},
            {{-1, 0}, {1, 0}},
            {{0, -1}, {1, 0}},
            {{0, 1}, {1, 0}},
            {{0, -1}, {-1, 0}},
            {{0, 1}, {-1, 0}}
        };
        int m = grid.length, n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{0, 0});
        seen[0][0] = true;
        while (!st.isEmpty()) {
            int[] cur = st.pop();
            int r = cur[0], c = cur[1];
            if (r == m - 1 && c == n - 1) return true;
            for (int[] d : dirs[grid[r][c]]) {
                int x = r + d[0], y = c + d[1];
                if (x < 0 || x >= m || y < 0 || y >= n || seen[x][y]) continue;
                boolean ok = false;
                for (int[] back : dirs[grid[x][y]]) {
                    if (back[0] == -d[0] && back[1] == -d[1]) ok = true;
                }
                if (ok) {
                    seen[x][y] = true;
                    st.push(new int[]{x, y});
                }
            }
        }
        return false;
    }
}
