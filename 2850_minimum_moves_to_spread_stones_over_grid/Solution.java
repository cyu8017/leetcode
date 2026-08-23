// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<int[]> extras;
    private List<int[]> zeros;
    private int best;

    public int minimumMoves(int[][] grid) {
        extras = new ArrayList<>();
        zeros = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) zeros.add(new int[] {i, j});
                else if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) extras.add(new int[] {i, j});
                }
            }
        }
        if (zeros.isEmpty()) return 0;
        best = 1 << 30;
        dfs(0, 0);
        return best;
    }

    private void dfs(int i, int cost) {
        if (cost >= best) return;
        if (i == zeros.size()) {
            best = cost;
            return;
        }
        for (int j = 0; j < extras.size(); j++) {
            if (extras.get(j)[0] < 0) continue;
            int[] e = extras.get(j);
            extras.set(j, new int[] {-1, e[1]});
            int d = Math.abs(e[0] - zeros.get(i)[0]) + Math.abs(e[1] - zeros.get(i)[1]);
            dfs(i + 1, cost + d);
            extras.set(j, e);
        }
    }
}
