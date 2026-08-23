// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

public class Solution {
    public long MostPoints(int[][] questions) {
        int n = questions.Length;
        long[] dp = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            int pts = questions[i][0], brain = questions[i][1];
            int next = i + brain + 1;
            long take = pts + (next < n ? dp[next] : 0);
            dp[i] = Math.Max(dp[i + 1], take);
        }
        return dp[0];
    }
}
