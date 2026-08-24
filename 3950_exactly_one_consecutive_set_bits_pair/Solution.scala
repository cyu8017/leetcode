// LeetCode 3950 - Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

object Solution {
  def consecutiveSetBits(n: Int): Boolean = {
    var vis = false
    var pre = 0
    var x = n
    while (x > 0) {
      val cur = x & 1
      if (pre == cur && cur == 1) {
        if (vis) return false
        vis = true
      }
      pre = cur
      x >>= 1
    }
    vis
  }
}
