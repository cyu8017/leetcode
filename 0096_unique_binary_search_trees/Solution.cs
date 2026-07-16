// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

public class Solution {
    public int NumTrees(int n) {
        var dp = new int[n + 1];
        dp[0] = 1;
        for (int nodes = 1; nodes <= n; nodes++) {
            for (int root = 1; root <= nodes; root++) {
                dp[nodes] += dp[root - 1] * dp[nodes - root];
            }
        }
        return dp[n];
    }
}
