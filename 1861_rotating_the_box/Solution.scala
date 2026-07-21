// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

object Solution {
  def rotateTheBox(boxGrid: Array[Array[Char]]): Array[Array[Char]] = {
    val m = boxGrid.length
    val n = boxGrid(0).length
    val rotated = Array.fill(n, m)('.')
    for (i <- 0 until n; j <- 0 until m) {
      rotated(i)(j) = boxGrid(m - 1 - j)(i)
    }
    for (col <- 0 until m) {
      var row = n - 1
      for (i <- n - 1 to 0 by -1) {
        if (rotated(i)(col) == '*') {
          row = i - 1
        } else if (rotated(i)(col) == '#') {
          rotated(i)(col) = '.'
          rotated(row)(col) = '#'
          row -= 1
        }
      }
    }
    rotated
  }
}
