// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

object Solution {
  def maximumTotalSum(maximumHeight: Array[Int]): Long = {
    val h = maximumHeight.sorted.reverse
    var ans = 0L
    var prev = 1000000000000000000L
    for (mh <- h) {
      var cur = mh.toLong
      if (cur >= prev) cur = prev - 1
      if (cur <= 0) return -1
      ans += cur
      prev = cur
    }
    ans
  }
}
