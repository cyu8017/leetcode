// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

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

class Solution(w: Array[Int]) {
  private val prefix: Array[Int] = {
    var runningTotal = 0
    w.map { weight =>
      runningTotal += weight
      runningTotal
    }
  }
  private val total: Int = prefix.lastOption.getOrElse(0)

  def pickIndex(): Int = {
    var target = SolutionSupport.uniform(0, total).toInt
    if (target >= total) {
      target = total - 1
    }
    bisectRight(prefix, target)
  }

  private def bisectRight(values: Array[Int], target: Int): Int = {
    var low = 0
    var high = values.length - 1
    while (low < high) {
      val mid = (low + high) / 2
      if (values(mid) <= target) {
        low = mid + 1
      } else {
        high = mid
      }
    }
    low
  }
}
