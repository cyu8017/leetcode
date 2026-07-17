// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

object Solution {
  def findBall(grid: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val ans = new Array[Int](n)
    for (start <- 0 until n) {
      var col = start
      var row = 0
      while (row < m && col != -1) {
        val next = col + grid(row)(col)
        if (next < 0 || next == n || grid(row)(next) != grid(row)(col)) {
          col = -1
        } else {
          col = next
        }
        row += 1
      }
      ans(start) = col
    }
    ans
  }
}
