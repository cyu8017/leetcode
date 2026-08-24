// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

object Solution {
  def minSizeSubarray(nums: Array[Int], target: Int): Int = {
    val n = nums.length
    var total = 0L
    nums.foreach(v => total += v)
    var ans = 1 << 30
    if (total > 0) {
      val loops = (target / total).toInt
      val remain = (target % total).toInt
      if (remain == 0) return loops * n
      val arr = nums ++ nums
      var left = 0
      var sum = 0
      var best = 1 << 30
      for (right <- arr.indices) {
        sum += arr(right)
        while (sum > remain && left <= right) {
          sum -= arr(left)
          left += 1
        }
        if (sum == remain && right - left + 1 < best) best = right - left + 1
      }
      if (best < (1 << 30)) ans = loops * n + best
    }
    if (ans == (1 << 30)) -1 else ans
  }
}
