// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

object Solution {
  private var dp: Array[Array[Array[Int]]] = _
  private var s: String = _

  def longestPalindromicSubsequence(s0: String, k: Int): Int = {
    s = s0
    val n = s.length
    dp = Array.fill(n, n, k + 1)(-1)
    dfs(0, n - 1, k)
  }

  private def distCirc(a: Char, b: Char): Int = {
    val d = math.abs(a - b)
    math.min(d, 26 - d)
  }

  private def dfs(i: Int, j: Int, ops: Int): Int = {
    if (i > j) return 0
    if (i == j) return 1
    if (dp(i)(j)(ops) != -1) return dp(i)(j)(ops)
    var best = dfs(i + 1, j, ops)
    best = math.max(best, dfs(i, j - 1, ops))
    val cost = distCirc(s.charAt(i), s.charAt(j))
    if (cost <= ops) best = math.max(best, 2 + dfs(i + 1, j - 1, ops - cost))
    dp(i)(j)(ops) = best
    best
  }
}
