// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int m, n;
    private int[][] grid;
    private final int[][] dirs = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
    private final int[] nextDir = {1, 2, 3, 0};
    private final Map<Long, Integer> memo = new HashMap<>();

    public int lenOfVDiagonal(int[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        memo.clear();
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1) continue;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dirs[d][0], nj = j + dirs[d][1];
                    int best = 1 + dfs(ni, nj, d, 0, 2);
                    if (best > ans) ans = best;
                }
                if (ans < 1) ans = 1;
            }
        }
        return ans;
    }

    private long key(int i, int j, int d, int turned, int expect) {
        return (((((long) i * 101L + j) * 5L + d) * 3L + turned) * 5L + expect);
    }

    private int dfs(int i, int j, int d, int turned, int expect) {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect) return 0;
        long k = key(i, j, d, turned, expect);
        Integer cached = memo.get(k);
        if (cached != null) return cached;
        int ni = i + dirs[d][0], nj = j + dirs[d][1];
        int nx = (expect == 2) ? 0 : 2;
        int best = 1 + dfs(ni, nj, d, turned, nx);
        if (turned == 0) {
            int nd = nextDir[d];
            int ti = i + dirs[nd][0], tj = j + dirs[nd][1];
            int cand = 1 + dfs(ti, tj, nd, 1, nx);
            if (cand > best) best = cand;
        }
        memo.put(k, best);
        return best;
    }
}
