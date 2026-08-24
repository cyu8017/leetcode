// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

object Solution {
  def secondsToRemoveOccurrences(s: String): Int = {
    var ans = 0
    var zeros = 0
    s.foreach { c =>
      if (c == '0') zeros += 1
      else if (zeros > 0) ans = math.max(ans + 1, zeros)
    }
    ans
  }
}
