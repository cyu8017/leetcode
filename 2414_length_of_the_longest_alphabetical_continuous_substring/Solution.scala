// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

object Solution {
  def longestContinuousSubstring(s: String): Int = {
    var ans = 1
    var cur = 1
    var i = 1
    while (i < s.length) {
      if (s.charAt(i) == s.charAt(i - 1) + 1) {
        cur += 1
        ans = math.max(ans, cur)
      } else cur = 1
      i += 1
    }
    ans
  }
}
