// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

object Solution {
  def minMoves(nums: Array[Int], k: Int): Int = {
    val adjusted = scala.collection.mutable.ArrayBuffer.empty[Long]
    for (i <- nums.indices) {
      if (nums(i) == 1) {
        adjusted += (i - adjusted.size).toLong
      }
    }
    val m = adjusted.size
    val prefix = new Array[Long](m + 1)
    for (i <- 0 until m) {
      prefix(i + 1) = prefix(i) + adjusted(i)
    }
    var best = Long.MaxValue
    for (left <- 0 to m - k) {
      val right = left + k
      val mid = left + k / 2
      val median = adjusted(mid)
      var cost = median * (mid - left) - (prefix(mid) - prefix(left))
      cost += (prefix(right) - prefix(mid + 1)) - median * (right - mid - 1)
      best = math.min(best, cost)
    }
    best.toInt
  }
}
