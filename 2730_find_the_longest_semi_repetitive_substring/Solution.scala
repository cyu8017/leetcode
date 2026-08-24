// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

object Solution {
  def longestSemiRepetitiveSubstring(s: String): Int = {
    var ans = 0
    var left = 0
    var lastPair = -1
    var right = 0
    while (right < s.length) {
      if (right > 0 && s.charAt(right) == s.charAt(right - 1)) {
        if (lastPair >= left) left = lastPair + 1
        lastPair = right - 1
      }
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
