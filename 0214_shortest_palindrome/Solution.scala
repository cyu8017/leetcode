// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

object Solution {
  def shortestPalindrome(s: String): String = {
    if (s.isEmpty) return ""
    val reversed = s.reverse
    val combined = s + "#" + reversed
    val pi = Array.fill(combined.length)(0)
    var lps = 0
    for (i <- 1 until combined.length) {
      while (lps > 0 && combined(i) != combined(lps)) lps = pi(lps - 1)
      if (combined(i) == combined(lps)) lps += 1
      pi(i) = lps
    }
    val prefixLen = pi(combined.length - 1)
    reversed.substring(0, s.length - prefixLen) + s
  }
}
