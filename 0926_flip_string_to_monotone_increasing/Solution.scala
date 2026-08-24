// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

object Solution {
  def minFlipsMonoIncr(s: String): Int = {
    var ones = 0
    var ans = 0
    s.foreach { ch =>
      if (ch == '1') ones += 1
      else ans = math.min(ans + 1, ones)
    }
    ans
  }
}
