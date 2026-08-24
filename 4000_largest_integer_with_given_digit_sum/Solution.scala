// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

object Solution {
  def largestInteger(n: Int, s0: Int): Int = {
    if (n * 9 < s0) return -1
    var s = s0
    var ans = 0
    var i = 0
    while (i < n) {
      val x = if (s < 9) s else 9
      ans = ans * 10 + x
      s -= x
      i += 1
    }
    ans
  }
}
