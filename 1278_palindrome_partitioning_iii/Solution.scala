// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

object Solution {
  def palindromePartition(s: String, k: Int): Int = {
    val n = s.length
    val cost = Array.ofDim[Int](n, n)
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      cost(i)(j) = (if (length > 2) cost(i + 1)(j - 1) else 0) + (if (s(i) != s(j)) 1 else 0)
    }
    val inf = n + 1
    val dp = Array.fill(k + 1, n + 1)(inf)
    dp(0)(0) = 0
    for (parts <- 1 to k; end <- parts to n) {
      dp(parts)(end) = (parts - 1 until end).map(start => dp(parts - 1)(start) + cost(start)(end - 1)).min
    }
    dp(k)(n)
  }
}
