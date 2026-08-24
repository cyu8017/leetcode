// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

object Solution {
  def validSubarraySize(nums: Array[Int], threshold: Int): Int = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      left(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
      i += 1
    }
    stack.clear()
    i = n - 1
    while (i >= 0) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      right(i) = if (stack.isEmpty) n else stack.last
      stack += i
      i -= 1
    }
    i = 0
    while (i < n) {
      val k = right(i) - left(i) - 1
      if (nums(i) > threshold / k) return k
      i += 1
    }
    -1
  }
}
