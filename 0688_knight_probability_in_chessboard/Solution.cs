// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

public class Solution {
    public double KnightProbability(int n, int k, int row, int column) {
        int[][] moves = {
            new[]{-2,-1}, new[]{-2,1}, new[]{-1,-2}, new[]{-1,2},
            new[]{1,-2}, new[]{1,2}, new[]{2,-1}, new[]{2,1}
        };
        double[][] dp = new double[n][];
        for (int i = 0; i < n; i++) dp[i] = new double[n];
        dp[row][column] = 1.0;
        for (int step = 0; step < k; step++) {
            double[][] nxt = new double[n][];
            for (int i = 0; i < n; i++) nxt[i] = new double[n];
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (dp[r][c] == 0.0) continue;
                    foreach (var move in moves) {
                        int nr = r + move[0], nc = c + move[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n) nxt[nr][nc] += dp[r][c] / 8.0;
                    }
                }
            }
            dp = nxt;
        }
        double total = 0.0;
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                total += dp[r][c];
        return total;
    }
}
