// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

object Solution {
  private def lowerBound(a: Array[Int], target: Long): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def minRemoval(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var cnt = 0
    var i = 0
    while (i < n) {
      var j = n
      if (1L * nums(i) * k <= nums(n - 1)) {
        val target = 1L * nums(i) * k + 1
        j = lowerBound(nums, target)
      }
      cnt = math.max(cnt, j - i)
      i += 1
    }
    n - cnt
  }
}
