// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

object Solution {
  def separateSquares(squares: Array[Array[Int]]): Double = {
    var total = 0.0
    squares.foreach { sq =>
      val l = sq(2).toDouble
      total += l * l
    }
    var lo = 0.0
    var hi = 2e9
    var it = 0
    while (it < 60) {
      val mid = (lo + hi) / 2
      if (areaBelow(squares, mid) * 2 < total) lo = mid
      else hi = mid
      it += 1
    }
    hi
  }

  private def areaBelow(squares: Array[Array[Int]], y: Double): Double = {
    var below = 0.0
    squares.foreach { sq =>
      val yi = sq(1).toDouble
      val l = sq(2).toDouble
      val top = yi + l
      if (y > yi) {
        if (y >= top) below += l * l
        else below += l * (y - yi)
      }
    }
    below
  }
}
