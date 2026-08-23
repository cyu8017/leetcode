// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

public class Solution {
    public int[][] SpecialGrid(int n) {
        int m = 1 << n;
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[m];
        int val = 0;
        void Dfs(int x, int y, int k) {
            if (k == 1) { ans[x][y] = val++; return; }
            int h = k / 2;
            Dfs(x, y, h);
            Dfs(x + h, y, h);
            Dfs(x + h, y - h, h);
            Dfs(x, y - h, h);
        }
        Dfs(0, m - 1, m);
        return ans;
    }
}
