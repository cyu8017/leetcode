// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

object Solution {
  def minOperations(s: String): Int = {
    var alt1 = 0
    for (i <- s.indices) {
      val expected = if ((i & 1) == 0) '0' else '1'
      if (s(i) != expected) {
        alt1 += 1
      }
    }
    math.min(alt1, s.length - alt1)
  }
}
