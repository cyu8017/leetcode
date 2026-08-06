// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

object Solution {
  def maxDistance(position: Array[Int], m: Int): Int = {
    val pos = position.sorted
    var lo = 1
    var hi = (pos.last - pos.head) / (m - 1)
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      var count = 1
      var last = pos(0)
      for (x <- pos.tail if x - last >= mid) {
        count += 1
        last = x
      }
      if (count >= m) lo = mid + 1 else hi = mid - 1
    }
    hi
  }
}
