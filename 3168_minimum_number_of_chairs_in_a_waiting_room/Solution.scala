// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

object Solution {
  def minimumChairs(s: String): Int = {
    var cnt = 0
    var left = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'E') {
        if (left > 0) left -= 1
        else cnt += 1
      } else left += 1
      i += 1
    }
    cnt
  }
}
