// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

import scala.collection.mutable

object Solution {
  def find132pattern(nums: Array[Int]): Boolean = {
    val stack = mutable.ArrayBuffer.empty[Int]
    var third = Int.MinValue
    nums.reverseIterator.foreach { value =>
      if (value < third) return true
      while (stack.nonEmpty && value > stack.last) {
        third = stack.remove(stack.length - 1)
      }
      stack += value
    }
    false
  }
}
