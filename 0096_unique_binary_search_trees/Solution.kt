// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

class Solution {
    fun numTrees(n: Int): Int {
        val dp = IntArray(n + 1)
        dp[0] = 1
        for (nodes in 1..n) {
            for (root in 1..nodes) {
                dp[nodes] += dp[root - 1] * dp[nodes - root]
            }
        }
        return dp[n]
    }
}
