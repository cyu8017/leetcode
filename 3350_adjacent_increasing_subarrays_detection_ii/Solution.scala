// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

object Solution {
  def maxIncreasingSubarrays(nums: Array[Int]): Int = {
    val n = nums.length
    val up = new Array[Int](n)
    up(n - 1) = 1
    var i = n - 2
    while (i >= 0) {
      up(i) = if (nums(i) < nums(i + 1)) up(i + 1) + 1 else 1
      i -= 1
    }
    var lo = 1
    var hi = n / 2
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(up, n, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(up: Array[Int], n: Int, k: Int): Boolean = {
    var i = 0
    while (i + 2 * k <= n) {
      if (up(i) >= k && up(i + k) >= k) return true
      i += 1
    }
    false
  }
}
