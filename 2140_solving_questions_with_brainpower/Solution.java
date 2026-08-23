// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            int pts = questions[i][0], brain = questions[i][1];
            int next = i + brain + 1;
            long take = pts + (next < n ? dp[next] : 0);
            dp[i] = Math.max(dp[i + 1], take);
        }
        return dp[0];
    }
}
