// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

class Solution {
    public long gridGame(int[][] grid) {
        int n = grid[0].length;
        long top = 0, bottom = 0, ans = Long.MAX_VALUE;
        for (int v : grid[0]) top += v;
        for (int i = 0; i < n; i++) {
            top -= grid[0][i];
            ans = Math.min(ans, Math.max(top, bottom));
            bottom += grid[1][i];
        }
        return ans;
    }
}
