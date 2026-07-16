// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

object SolutionSupport {
  private var uniformFn: (Double, Double) => Double = (_, _) => 0.0

  def set_uniform(fn: (Double, Double) => Double): Unit = {
    uniformFn = fn
  }

  def setUniform(fn: (Double, Double) => Double): Unit = set_uniform(fn)

  def setSequence(values: Array[Double]): Unit = {
    var index = 0
    set_uniform((_, _) => {
      val value = values(index)
      index += 1
      value
    })
  }

  def uniform(a: Double, b: Double): Double = uniformFn(a, b)
}

class Solution(m: Int, n: Int) {
  private val cols = n
  private val total = m * n
  private var available = mutable.ArrayBuffer.empty[Int]

  reset()

  def flip(): Array[Int] = {
    var index = SolutionSupport.uniform(0, available.size - 1).toInt
    if (index >= available.size) {
      index = available.size - 1
    }
    val value = available(index)
    available(index) = available.last
    available.remove(available.size - 1)
    Array(value / cols, value % cols)
  }

  def reset(): Unit = {
    available = mutable.ArrayBuffer.from(0 until total)
  }
}
