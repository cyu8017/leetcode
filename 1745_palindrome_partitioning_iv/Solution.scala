// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

object Solution {
  def checkPartitioning(s: String): Boolean = {
    val n = s.length
    val pal = Array.ofDim[Boolean](n, n)
    for (i <- n - 1 to 0 by -1; j <- i until n) {
      pal(i)(j) = s(i) == s(j) && (j - i < 2 || pal(i + 1)(j - 1))
    }
    for (i <- 0 until n - 2; j <- i + 1 until n - 1) {
      if (pal(0)(i) && pal(i + 1)(j) && pal(j + 1)(n - 1)) {
        return true
      }
    }
    false
  }
}
