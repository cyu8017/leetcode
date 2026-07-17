// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

object Solution {
  def minimumBoxes(n: Int): Int = {
    var height = 0L
    var used = 0L
    var base = 0L
    while (used + (height + 1) * (height + 2) / 2 <= n) {
      height += 1
      val layer = height * (height + 1) / 2
      used += layer
      base += height
    }
    var extra = 0L
    while (used < n) {
      extra += 1
      used += extra
    }
    (base + extra).toInt
  }
}
