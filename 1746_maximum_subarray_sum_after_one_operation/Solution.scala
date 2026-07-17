// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

object Solution {
  def maxSumAfterOperation(nums: Array[Int]): Int = {
    var noSquare = 0L
    var oneSquare = 0L
    var best = Long.MinValue
    for (value <- nums) {
      val v = value.toLong
      oneSquare = math.max(math.max(oneSquare + v, noSquare + v * v), v * v)
      noSquare = math.max(noSquare + v, v)
      best = math.max(best, oneSquare)
    }
    best.toInt
  }
}
