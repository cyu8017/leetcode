// LeetCode 1037 - Valid Boomerang
// https://leetcode.com/problems/valid-boomerang/

object Solution {
  def isBoomerang(points: Array[Array[Int]]): Boolean = {
    val x1 = points(0)(0); val y1 = points(0)(1)
    val x2 = points(1)(0); val y2 = points(1)(1)
    val x3 = points(2)(0); val y3 = points(2)(1)
    (x2 - x1).toLong * (y3 - y1) != (x3 - x1).toLong * (y2 - y1)
  }
}
