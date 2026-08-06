// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

trait CustomFunction {
  def f(x: Int, y: Int): Int
}

object Solution {
  def findSolution(customfunction: CustomFunction, z: Int): List[List[Int]] = {
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    var x = 1
    var y = 1000
    while (x <= 1000 && y >= 1) {
      val value = customfunction.f(x, y)
      if (value == z) {
        answer += List(x, y)
        x += 1
        y -= 1
      } else if (value < z) x += 1
      else y -= 1
    }
    answer.toList
  }
}
