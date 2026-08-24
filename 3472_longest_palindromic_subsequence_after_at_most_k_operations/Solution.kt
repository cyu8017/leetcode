// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

class Solution {
    private lateinit var dp: Array<Array<IntArray>>
    private lateinit var s: String

    fun longestPalindromicSubsequence(s: String, k: Int): Int {
        this.s = s
        val n = s.length
        dp = Array(n) { Array(n) { IntArray(k + 1) { -1 } } }
        return dfs(0, n - 1, k)
    }

    private fun distCirc(a: Char, b: Char): Int {
        val d = kotlin.math.abs(a - b)
        return minOf(d, 26 - d)
    }

    private fun dfs(i: Int, j: Int, ops: Int): Int {
        if (i > j) return 0
        if (i == j) return 1
        if (dp[i][j][ops] != -1) return dp[i][j][ops]
        var best = dfs(i + 1, j, ops)
        best = maxOf(best, dfs(i, j - 1, ops))
        val cost = distCirc(s[i], s[j])
        if (cost <= ops) best = maxOf(best, 2 + dfs(i + 1, j - 1, ops - cost))
        dp[i][j][ops] = best
        return best
    }
}
