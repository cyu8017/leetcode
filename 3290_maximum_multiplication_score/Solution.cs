// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

public class Solution {
    public long MaxScore(int[] a, int[] b) {
        long neg = -(1L << 62);
        long[] dp = new long[] { 0, neg, neg, neg, neg };
        foreach (int x in b) {
            for (int k = 4; k >= 1; k--) {
                if (dp[k - 1] == neg) continue;
                long v = dp[k - 1] + (long)a[k - 1] * x;
                if (v > dp[k]) dp[k] = v;
            }
        }
        return dp[4];
    }
}
