// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

object Solution {
  def maxOperations(s: String): Int = {
    var ans = 0
    var cnt = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '1') cnt += 1
      else if (i > 0 && s.charAt(i - 1) == '1') ans += cnt
      i += 1
    }
    ans
  }
}
