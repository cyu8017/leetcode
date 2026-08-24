// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

object Solution {
  def minOperations(s1: String, s2: String, x: Int): Int = {
    val diff = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- s1.indices if s1.charAt(i) != s2.charAt(i)) diff += i
    val m = diff.length
    if (m % 2 == 1) return -1
    if (m == 0) return 0
    val dp2 = Array.fill(m + 1)(1 << 30)
    dp2(0) = 0
    for (i <- 0 until m) {
      if (dp2(i) < (1 << 30) && i + 1 < m) {
        var cand = diff(i + 1) - diff(i)
        if (cand > x) cand = x
        if (dp2(i) + cand < dp2(i + 2)) dp2(i + 2) = dp2(i) + cand
      }
    }
    if (dp2(m) >= (1 << 30)) -1 else dp2(m)
  }
}
