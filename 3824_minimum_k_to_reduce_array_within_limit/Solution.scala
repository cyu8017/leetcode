// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum_k_to_reduce_array_within_limit/

object Solution {
  def minimumK(nums: Array[Int]): Int = {
    var lo = 1
    var hi = 100000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (check(nums, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def check(nums: Array[Int], k: Int): Boolean = {
    var t = 0L
    nums.foreach { x => t += (x + k - 1L) / k }
    t <= 1L * k * k
  }
}
