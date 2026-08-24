// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

object Solution {
  def fallingSquares(positions: Array[Array[Int]]): List[Int] = {
    val intervals = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    val answer = scala.collection.mutable.ArrayBuffer.empty[Int]
    var maxHeight = 0
    for (pos <- positions) {
      val left = pos(0)
      val side = pos(1)
      val right = left + side
      var bas = 0
      for (it <- intervals) {
        if (it(1) > left && it(0) < right) bas = math.max(bas, it(2))
      }
      val height = bas + side
      intervals += Array(left, right, height)
      maxHeight = math.max(maxHeight, height)
      answer += maxHeight
    }
    answer.toList
  }
}
