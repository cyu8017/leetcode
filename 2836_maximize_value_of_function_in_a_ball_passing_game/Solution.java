// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
    public long getMaxFunctionValue(int[] receiver, long k) {
        int n = receiver.length;
        final int LOG = 36;
        int[][] up = new int[LOG][n];
        long[][] sum = new long[LOG][n];
        for (int i = 0; i < n; i++) {
            up[0][i] = receiver[i];
            sum[0][i] = receiver[i];
        }
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                int mid = up[j - 1][i];
                up[j][i] = up[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = i;
            long total = i;
            long kk = k;
            for (int j = 0; j < LOG; j++) {
                if ((kk & (1L << j)) != 0) {
                    total += sum[j][cur];
                    cur = up[j][cur];
                }
            }
            ans = Math.max(ans, total);
        }
        return ans;
    }
}
