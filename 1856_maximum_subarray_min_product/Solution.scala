// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

import scala.collection.mutable

object Solution {
  def maxSumMinProduct(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    val prefix = Array.ofDim[Long](n + 1)
    for (i <- nums.indices) {
      prefix(i + 1) = prefix(i) + nums(i)
    }

    val leftBound = Array.fill(n)(-1)
    val stack = mutable.ArrayBuffer.empty[Int]
    for (i <- nums.indices) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) {
        stack.remove(stack.length - 1)
      }
      leftBound(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
    }

    val rightBound = Array.fill(n)(n)
    stack.clear()
    for (i <- n - 1 to 0 by -1) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) {
        stack.remove(stack.length - 1)
      }
      rightBound(i) = if (stack.isEmpty) n else stack.last
      stack += i
    }

    var best = 0L
    for (i <- nums.indices) {
      val total = prefix(rightBound(i)) - prefix(leftBound(i) + 1)
      best = math.max(best, total * nums(i))
    }
    (best % mod).toInt
  }
}
