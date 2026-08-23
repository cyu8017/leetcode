// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

public class Solution {
    public bool IsPossibleToCutPath(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        bool Dfs(int r, int c) {
            if (r == m - 1 && c == n - 1) return true;
            if (r >= m || c >= n || grid[r][c] == 0) return false;
            if (!(r == 0 && c == 0)) grid[r][c] = 0;
            return Dfs(r + 1, c) || Dfs(r, c + 1);
        }
        if (!Dfs(0, 0)) return true;
        grid[0][0] = 1;
        return !Dfs(0, 0);
    }
}
