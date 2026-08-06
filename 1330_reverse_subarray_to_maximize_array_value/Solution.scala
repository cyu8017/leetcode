// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

object Solution {
  def maxValueAfterReverse(nums: Array[Int]): Int = {
    var base = 0
    for (i <- 0 until nums.length - 1) base += math.abs(nums(i) - nums(i + 1))
    var gain = 0
    var low = Int.MaxValue
    var high = Int.MinValue
    for (i <- 0 until nums.length - 1) {
      val a = nums(i)
      val b = nums(i + 1)
      gain = math.max(gain, math.max(
        math.abs(nums(0) - b) - math.abs(a - b),
        math.abs(nums(nums.length - 1) - a) - math.abs(a - b)
      ))
      low = math.min(low, math.max(a, b))
      high = math.max(high, math.min(a, b))
    }
    base + math.max(gain, 2 * (high - low))
  }
}
