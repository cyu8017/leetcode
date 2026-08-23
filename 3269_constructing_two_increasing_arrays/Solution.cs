// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

public class Solution {
    public int MinLargest(int[] nums1, int[] nums2) {
        int n = nums1.Length, m = nums2.Length;
        const int inf = 1000000000;
        int[][] dp = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new int[m + 1];
            for (int j = 0; j <= m; j++) dp[i][j] = inf;
        }
        dp[0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (dp[i][j] == inf) continue;
                int prev = dp[i][j];
                if (i < n) {
                    int need = prev + 1;
                    if (nums1[i] == 0) {
                        if (need % 2 != 0) need++;
                    } else {
                        if (need % 2 == 0) need++;
                    }
                    if (need < dp[i + 1][j]) dp[i + 1][j] = need;
                }
                if (j < m) {
                    int need = prev + 1;
                    if (nums2[j] == 0) {
                        if (need % 2 != 0) need++;
                    } else {
                        if (need % 2 == 0) need++;
                    }
                    if (need < dp[i][j + 1]) dp[i][j + 1] = need;
                }
            }
        }
        return dp[n][m];
    }
}
