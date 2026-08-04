// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

class Solution {
    public int maxSizeSlices(int[] slices) {
        int k = slices.length / 3;
        return Math.max(line(slices, 0, slices.length - 1, k), line(slices, 1, slices.length, k));
    }

    private int line(int[] slices, int start, int end, int k) {
        int n = end - start;
        int[] a = new int[n];
        System.arraycopy(slices, start, a, 0, n);
        int[][] dp = new int[n + 2][k + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i + 2][j] = Math.max(dp[i + 1][j], dp[i][j - 1] + a[i]);
            }
        }
        return dp[n + 1][k];
    }
}
