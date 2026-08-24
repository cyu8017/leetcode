// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

object Solution {
  def shiftDistance(s: String, t: String, nextCost: Array[Int], previousCost: Array[Int]): Long = {
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val a = s.charAt(i) - 'a'
      val b = t.charAt(i) - 'a'
      if (a != b) {
        var fwd = 0L
        var x = a
        while (x != b) {
          fwd += nextCost(x)
          x = (x + 1) % 26
        }
        var bwd = 0L
        x = a
        while (x != b) {
          bwd += previousCost(x)
          x = (x + 25) % 26
        }
        ans += (if (fwd < bwd) fwd else bwd)
      }
      i += 1
    }
    ans
  }
}
