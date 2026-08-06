// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

object Solution {
  def checkStraightLine(coordinates: Array[Array[Int]]): Boolean = {
    val x0 = coordinates(0)(0)
    val y0 = coordinates(0)(1)
    val dx = coordinates(1)(0) - x0
    val dy = coordinates(1)(1) - y0
    coordinates.drop(2).forall { p =>
      (p(0) - x0).toLong * dy == (p(1) - y0).toLong * dx
    }
  }
}
