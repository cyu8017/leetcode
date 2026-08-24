// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

object Solution {
  def countSubstrings(s: String, c: Char): Long = {
    var cnt = 0L
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == c) cnt += 1
      i += 1
    }
    cnt * (cnt + 1) / 2
  }
}
