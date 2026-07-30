// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

using System;

public class Solution {
    public int MinimumMoves(int[] arr) {
        int n = arr.Length;
        var dp = new int[n, n];
        for (int i = 0; i < n; i++) dp[i, i] = 1;
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i, j] = 1 + dp[i + 1, j];
                if (arr[i] == arr[i + 1]) {
                    dp[i, j] = Math.Min(dp[i, j], 1 + (i + 2 <= j ? dp[i + 2, j] : 0));
                }
                for (int k = i + 2; k <= j; k++) {
                    if (arr[i] == arr[k]) {
                        dp[i, j] = Math.Min(dp[i, j],
                            dp[i + 1, k - 1] + (k < j ? dp[k + 1, j] : 0));
                    }
                }
            }
        }
        return dp[0, n - 1];
    }
}
