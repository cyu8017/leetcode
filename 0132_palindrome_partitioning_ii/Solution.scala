// LeetCode 0132 - Palindrome Partitioning II
// https://leetcode.com/problems/palindrome-partitioning-ii/

object Solution {
  def minCut(s: String): Int = {
    val n = s.length
    if (n == 0) return 0
    val isPalindrome = Array.ofDim[Boolean](n, n)
    for (left <- (n - 1) to 0 by -1; right <- left until n)
      isPalindrome(left)(right) = s(left) == s(right) && (right - left < 2 || isPalindrome(left + 1)(right - 1))
    val cuts = Array.ofDim[Int](n)
    for (end <- 0 until n) {
      cuts(end) = end
      if (isPalindrome(0)(end)) cuts(end) = 0
      else for (start <- 0 until end if isPalindrome(start + 1)(end)) cuts(end) = math.min(cuts(end), cuts(start) + 1)
    }
    cuts(n - 1)
  }
}
