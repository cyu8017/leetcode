// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0 && flood(grid, r, c)) answer++;
            }
        }
        return answer;
    }

    private boolean flood(int[][] grid, int sr, int sc) {
        int m = grid.length, n = grid[0].length;
        boolean closed = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int[] stackR = new int[m * n], stackC = new int[m * n];
        int top = 0;
        stackR[top] = sr;
        stackC[top] = sc;
        grid[sr][sc] = 1;
        while (top >= 0) {
            int r = stackR[top], c = stackC[top];
            top--;
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    top++;
                    stackR[top] = nr;
                    stackC[top] = nc;
                }
            }
        }
        return closed;
    }
}

