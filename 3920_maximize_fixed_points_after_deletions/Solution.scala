// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

object Solution {
  def maxFixedPoints(nums: Array[Int]): Int = {
    val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (i >= nums(i)) {
        val d = i - nums(i)
        var lo = 0
        var hi = tails.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (tails(mid) < d) lo = mid + 1
          else hi = mid
        }
        if (lo == tails.length) tails += d
        else tails(lo) = d
      }
      i += 1
    }
    tails.length
  }
}
