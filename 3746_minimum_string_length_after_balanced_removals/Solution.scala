// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

object Solution {
  def minLengthAfterRemovals(s: String): Int = {
    var a = 0
    s.foreach(c => if (c == 'a') a += 1)
    val b = s.length - a
    math.abs(a - b)
  }
}
