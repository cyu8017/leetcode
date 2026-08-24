// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

object Solution {
  def countBinarySubstrings(s: String): Int = {
    var prev = 0
    var cur = 1
    var ans = 0
    var i = 1
    while (i < s.length) {
      if (s.charAt(i) == s.charAt(i - 1)) cur += 1
      else {
        ans += math.min(prev, cur)
        prev = cur
        cur = 1
      }
      i += 1
    }
    ans + math.min(prev, cur)
  }
}
