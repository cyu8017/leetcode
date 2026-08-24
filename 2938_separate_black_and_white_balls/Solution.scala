// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

object Solution {
  def minimumSteps(s: String): Long = {
    var ans = 0L
    var zeros = 0L
    var i = s.length - 1
    while (i >= 0) {
      if (s.charAt(i) == '0') zeros += 1
      else ans += zeros
      i -= 1
    }
    ans
  }
}
