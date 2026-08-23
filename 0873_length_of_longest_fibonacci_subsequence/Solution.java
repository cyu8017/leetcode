// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

import java.util.*;

class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < n; i++) index.put(arr[i], i);
        int[][] dp = new int[n][n];
        for (int[] row : dp) Arrays.fill(row, 2);
        int ans = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < j; i++) {
                Integer k = index.get(arr[j] - arr[i]);
                if (k != null && k < i) {
                    dp[i][j] = dp[k][i] + 1;
                    ans = Math.max(ans, dp[i][j]);
                }
            }
        }
        return ans >= 3 ? ans : 0;
    }
}
