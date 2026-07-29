// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

object Solution {
  def validSubarrays(nums: Array[Int]): Int = {
    val stack = scala.collection.mutable.Stack.empty[Int]
    var ans = 0
    for (i <- nums.indices) {
      while (stack.nonEmpty && nums(stack.top) > nums(i)) {
        val j = stack.pop()
        ans += i - j
      }
      stack.push(i)
    }
    while (stack.nonEmpty) {
      val j = stack.pop()
      ans += nums.length - j
    }
    ans
  }
}
