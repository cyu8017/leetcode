// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

using System.Collections.Generic;

public class Solution {
    public long MaximumBooks(int[] books) {
        int n = books.Length;
        long[] dp = new long[n];
        var stack = new List<int>();
        long ans = 0;
        long Sum(int l, int r, int h) {
            int width = r - l + 1;
            if (h >= width) return (long)width * (2L * h - width + 1) / 2;
            return (long)h * (h + 1) / 2;
        }
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && books[stack[stack.Count - 1]] >= books[i] - (i - stack[stack.Count - 1]))
                stack.RemoveAt(stack.Count - 1);
            if (stack.Count == 0) dp[i] = Sum(0, i, books[i]);
            else {
                int j = stack[stack.Count - 1];
                dp[i] = dp[j] + Sum(j + 1, i, books[i]);
            }
            if (dp[i] > ans) ans = dp[i];
            stack.Add(i);
        }
        return ans;
    }
}
