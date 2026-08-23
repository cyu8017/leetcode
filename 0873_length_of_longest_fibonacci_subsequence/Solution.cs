// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

using System;
using System.Collections.Generic;

public class Solution {
    public int LenLongestFibSubseq(int[] arr) {
        int n = arr.Length;
        var index = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) index[arr[i]] = i;
        int[][] dp = new int[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[n];
            for (int j = 0; j < n; j++) dp[i][j] = 2;
        }
        int ans = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (index.TryGetValue(arr[j] - arr[i], out int k) && k < i) {
                    dp[i][j] = dp[k][i] + 1;
                    ans = Math.Max(ans, dp[i][j]);
                }
            }
        }
        return ans >= 3 ? ans : 0;
    }
}
