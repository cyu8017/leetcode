// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

object Solution {
  def minCapability(nums: Array[Int], k: Int): Int = {
    var lo = Int.MaxValue
    var hi = Int.MinValue
    nums.foreach { x =>
      if (x < lo) lo = x
      if (x > hi) hi = x
    }
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, k, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(nums: Array[Int], k: Int, cap: Int): Boolean = {
    var cnt = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) <= cap) {
        cnt += 1
        i += 2
      } else i += 1
    }
    cnt >= k
  }
}
