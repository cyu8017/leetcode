// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

import scala.collection.mutable

object Solution {
  def nextGreaterElements(nums: Array[Int]): Array[Int] = {
    val length = nums.length
    val result = Array.fill(length)(-1)
    val stack = mutable.ArrayBuffer.empty[Int]
    for (index <- 0 until length * 2) {
      val value = nums(index % length)
      while (stack.nonEmpty && nums(stack.last) < value) result(stack.remove(stack.length - 1)) = value
      if (index < length) stack += index
    }
    result
  }
}
