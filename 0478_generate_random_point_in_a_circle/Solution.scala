// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

import scala.util.Random

object SolutionSupport {
  private var uniformFn: (Double, Double) => Double = (a, b) => (b - a) * Random.nextDouble() + a

  def setUniform(fn: (Double, Double) => Double): Unit = {
    uniformFn = fn
  }

  def uniform(a: Double, b: Double): Double = uniformFn(a, b)
}

class Solution(radius: Double, xCenter: Double, yCenter: Double) {
  private val circleRadius = radius
  private val centerX = xCenter
  private val centerY = yCenter

  def randPoint(): Array[Double] = {
    while (true) {
      val x = SolutionSupport.uniform(-circleRadius, circleRadius)
      val y = SolutionSupport.uniform(-circleRadius, circleRadius)
      if (x * x + y * y <= circleRadius * circleRadius) {
        return Array(
          BigDecimal(centerX + x).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble,
          BigDecimal(centerY + y).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble
        )
      }
    }
    Array.empty[Double]
  }
}
