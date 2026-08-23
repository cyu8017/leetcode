// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    public int minXor(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        var dp = new boolean[cols][];
        for (int i = 0; i < cols; i++) dp[i] = new boolean[1024];
        for (int row = 0; row < rows; row++) {
            var left = new boolean[1024];
            for (int col = 0; col < cols; col++) {
                var next = new boolean[1024];
                int value = grid[row][col];
                if (row == 0 && col == 0) {
                    next[value] = true;
                } else {
                    for (int xorv = 0; xorv < 1024; xorv++) {
                        if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true;
                    }
                }
                dp[col] = next;
                left = next;
            }
        }
        for (int xorv = 0; xorv < 1024; xorv++) {
            if (dp[cols - 1][xorv]) return xorv;
        }
        return -1;
    }
}
