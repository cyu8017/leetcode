// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

object Solution {
  def totalSteps(nums: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var ans = 0
    var i = nums.length - 1
    while (i >= 0) {
      var steps = 0
      while (stack.nonEmpty && nums(i) > stack.last(0)) {
        steps = math.max(steps, stack.last(1))
        stack.remove(stack.length - 1)
        steps += 1
      }
      ans = math.max(ans, steps)
      stack += Array(nums(i), steps)
      i -= 1
    }
    ans
  }
}
