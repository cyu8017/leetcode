// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

public class Solution {
    public int CountSubIslands(int[][] grid1, int[][] grid2) {
        int rows = grid2.Length, cols = grid2[0].Length;
        bool Dfs(int r, int c) {
            if (r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0) return true;
            grid2[r][c] = 0;
            bool ok = grid1[r][c] == 1;
            if (!Dfs(r + 1, c)) ok = false;
            if (!Dfs(r - 1, c)) ok = false;
            if (!Dfs(r, c + 1)) ok = false;
            if (!Dfs(r, c - 1)) ok = false;
            return ok;
        }
        int ans = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid2[r][c] == 1 && Dfs(r, c)) ans++;
        return ans;
    }
}