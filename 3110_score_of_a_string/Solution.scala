// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

object Solution {
  def scoreOfString(s: String): Int = {
    var ans = 0
    var i = 1
    while (i < s.length) {
      ans += math.abs(s.charAt(i - 1) - s.charAt(i))
      i += 1
    }
    ans
  }
}
