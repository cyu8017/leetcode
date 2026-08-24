// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

object Solution {
  def maxWidthRamp(nums: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    while (i < nums.length) {
      if (stack.isEmpty || nums(stack.last) > nums(i)) stack += i
      i += 1
    }
    var ans = 0
    var j = nums.length - 1
    while (j >= 0) {
      while (stack.nonEmpty && nums(stack.last) <= nums(j)) {
        ans = math.max(ans, j - stack.last)
        stack.remove(stack.length - 1)
      }
      j -= 1
    }
    ans
  }
}
