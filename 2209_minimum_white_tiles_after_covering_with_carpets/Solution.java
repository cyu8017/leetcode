// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution {
    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        int n = floor.length();
        int[][] dp = new int[numCarpets + 1][n + 1];
        for (int i = 0; i <= numCarpets; i++)
            for (int j = 0; j <= n; j++)
                dp[i][j] = 1 << 30;
        dp[0][0] = 0;
        for (int j = 1; j <= n; j++)
            dp[0][j] = dp[0][j - 1] + (floor.charAt(j - 1) == '1' ? 1 : 0);
        for (int c = 1; c <= numCarpets; c++) {
            dp[c][0] = 0;
            for (int j = 1; j <= n; j++) {
                dp[c][j] = dp[c][j - 1] + (floor.charAt(j - 1) == '1' ? 1 : 0);
                int start = Math.max(0, j - carpetLen);
                dp[c][j] = Math.min(dp[c][j], dp[c - 1][start]);
            }
        }
        return dp[numCarpets][n];
    }
}
