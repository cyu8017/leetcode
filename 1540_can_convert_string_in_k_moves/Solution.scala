// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

object Solution {
  def canConvertString(s: String, t: String, k: Int): Boolean = {
    if (s.length != t.length) return false
    val used = Array.fill(26)(0)
    for (i <- s.indices) {
      val shift = (t(i) - s(i) + 26) % 26
      if (shift != 0) {
        used(shift) += 1
        if (shift + 26L * (used(shift) - 1) > k) return false
      }
    }
    true
  }
}
