// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public long maximumBooks(int[] books) {
        int n = books.length;
        long[] dp = new long[n];
        Deque<Integer> stack = new ArrayDeque<>();
        long ans = 0;
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && books[stack.peek()] >= books[i] - (i - stack.peek())) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                dp[i] = sum(0, i, books[i]);
            } else {
                int j = stack.peek();
                dp[i] = dp[j] + sum(j + 1, i, books[i]);
            }
            ans = Math.max(ans, dp[i]);
            stack.push(i);
        }
        return ans;
    }

    private long sum(int l, int r, int h) {
        int width = r - l + 1;
        if (h >= width) return (long) width * (2L * h - width + 1) / 2;
        return (long) h * (h + 1) / 2;
    }
}
