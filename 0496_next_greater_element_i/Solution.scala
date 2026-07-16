// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

import scala.collection.mutable

object Solution {
  def nextGreaterElement(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val nextGreater = mutable.Map.empty[Int, Int]
    val stack = mutable.ArrayBuffer.empty[Int]
    for (num <- nums2) {
      while (stack.nonEmpty && stack.last < num) nextGreater(stack.remove(stack.length - 1)) = num
      stack += num
    }
    nums1.map(num => nextGreater.getOrElse(num, -1))
  }
}
