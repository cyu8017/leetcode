// LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

object Solution {
  def findTheLongestBalancedSubstring(s: String): Int = {
    var ans = 0
    var zeros = 0
    var ones = 0
    s.foreach { c =>
      if (c == '0') {
        if (ones > 0) {
          zeros = 0
          ones = 0
        }
        zeros += 1
      } else {
        ones += 1
        val cur = math.min(ones, zeros)
        if (2 * cur > ans) ans = 2 * cur
      }
    }
    ans
  }
}
