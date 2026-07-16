// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

import scala.collection.mutable.ArrayBuffer

object Solution {
  def largestRectangleArea(heights: Array[Int]): Int = {
    val stack = ArrayBuffer.empty[Int]
    var maxArea = 0
    val extended = heights :+ 0

    var i = 0
    while (i < extended.length) {
      val height = extended(i)
      while (stack.nonEmpty && extended(stack.last) > height) {
        val h = extended(stack.remove(stack.length - 1))
        val width = if (stack.isEmpty) i else i - stack.last - 1
        maxArea = math.max(maxArea, h * width)
      }
      stack += i
      i += 1
    }

    maxArea
  }
}
