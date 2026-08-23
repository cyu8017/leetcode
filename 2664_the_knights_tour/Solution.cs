// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

public class Solution {
    public int[][] TourOfKnight(int m, int n, int r, int c) {
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) {
            ans[i] = new int[n];
            for (int j = 0; j < n; j++) ans[i][j] = -1;
        }
        int[][] dirs = { new[]{1,2}, new[]{1,-2}, new[]{-1,2}, new[]{-1,-2}, new[]{2,1}, new[]{2,-1}, new[]{-2,1}, new[]{-2,-1} };
        bool Dfs(int x, int y, int step) {
            ans[x][y] = step;
            if (step == m * n - 1) return true;
            foreach (var d in dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1)
                    if (Dfs(nx, ny, step + 1)) return true;
            }
            ans[x][y] = -1;
            return false;
        }
        Dfs(r, c, 0);
        return ans;
    }
}
