// LeetCode 3976 - Maximum Subarray Sum After Multiplier
// https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

object Solution {
  def maxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val inf = Long.MinValue / 4
    val f = Array.fill(n + 1, 4)(inf)
    f(0)(0) = 0
    var ans = inf
    var i = 1
    while (i <= n) {
      val x = nums(i - 1).toLong
      f(i)(0) = math.max(f(i - 1)(0), 0L) + x
      f(i)(1) = math.max(math.max(f(i - 1)(0), f(i - 1)(1)), 0L) + x * k
      f(i)(2) = math.max(math.max(f(i - 1)(0), f(i - 1)(2)), 0L) + x / k
      f(i)(3) = math.max(math.max(f(i - 1)(1), f(i - 1)(2)), f(i - 1)(3)) + x
      ans = math.max(ans, math.max(math.max(f(i)(0), f(i)(1)), math.max(f(i)(2), f(i)(3))))
      i += 1
    }
    ans
  }
}
