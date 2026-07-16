// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

import scala.collection.mutable.ArrayBuffer

object Solution {
  def maximalRectangle(matrix: Array[Array[Char]]): Int = {
    if (matrix.isEmpty) {
      return 0
    }

    val cols = matrix(0).length
    val heights = Array.fill(cols)(0)
    var maxArea = 0

    var r = 0
    while (r < matrix.length) {
      var j = 0
      while (j < cols) {
        heights(j) = if (matrix(r)(j) == '1') heights(j) + 1 else 0
        j += 1
      }
      maxArea = math.max(maxArea, largestHistogram(heights))
      r += 1
    }

    maxArea
  }

  private def largestHistogram(heights: Array[Int]): Int = {
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
