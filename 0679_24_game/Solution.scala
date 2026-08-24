// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

import scala.collection.mutable

object Solution {
  private val EPS = 1e-6

  def judgePoint24(cards: Array[Int]): Boolean = {
    val nums = mutable.ArrayBuffer.from(cards.map(_.toDouble))
    dfs(nums)
  }

  private def dfs(nums: mutable.ArrayBuffer[Double]): Boolean = {
    if (nums.size == 1) return math.abs(nums(0) - 24.0) < EPS
    var i = 0
    while (i < nums.size) {
      var j = 0
      while (j < nums.size) {
        if (i != j) {
          val rest = mutable.ArrayBuffer.empty[Double]
          var k = 0
          while (k < nums.size) {
            if (k != i && k != j) rest += nums(k)
            k += 1
          }
          val a = nums(i)
          val b = nums(j)
          val candidates = mutable.ArrayBuffer(a + b, a - b, a * b)
          if (math.abs(b) > EPS) candidates += a / b
          candidates.foreach { value =>
            rest += value
            if (dfs(rest)) return true
            rest.remove(rest.size - 1)
          }
        }
        j += 1
      }
      i += 1
    }
    false
  }
}
