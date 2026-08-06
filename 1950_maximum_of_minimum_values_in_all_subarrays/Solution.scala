// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

object Solution {
  def findMaximums(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val left = Array.fill(n)(-1)
    val right = Array.fill(n)(n)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- nums.indices) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      left(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
    }
    stack.clear()
    for (i <- n - 1 to 0 by -1) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      right(i) = if (stack.isEmpty) n else stack.last
      stack += i
    }
    val ans = Array.ofDim[Int](n)
    for (i <- nums.indices) {
      val length = right(i) - left(i) - 1
      ans(length - 1) = math.max(ans(length - 1), nums(i))
    }
    for (i <- n - 2 to 0 by -1) ans(i) = math.max(ans(i), ans(i + 1))
    ans
  }
}
