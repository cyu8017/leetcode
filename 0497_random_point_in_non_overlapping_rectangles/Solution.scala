// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

object SolutionSupport {
  private var uniformFn: (Double, Double) => Double = (a, b) => a

  def setUniform(fn: (Double, Double) => Double): Unit = {
    uniformFn = fn
  }

  def uniform(a: Double, b: Double): Double = uniformFn(a, b)
}

class Solution(rects: Array[Array[Int]]) {
  private val total: Int = {
    var areaTotal = 0
    for (rect <- rects) {
      val width = rect(2) - rect(0) + 1
      val height = rect(3) - rect(1) + 1
      areaTotal += width * height
    }
    areaTotal
  }

  def pick(): Array[Int] = {
    var index = SolutionSupport.uniform(0, total).toInt
    if (index >= total) index = total - 1
    for (rect <- rects) {
      val width = rect(2) - rect(0) + 1
      val height = rect(3) - rect(1) + 1
      val size = width * height
      if (index < size) {
        val offsetX = index % width
        val offsetY = index / width
        return Array(rect(0) + offsetX, rect(1) + offsetY)
      }
      index -= size
    }
    Array(rects.last(0), rects.last(1))
  }
}
