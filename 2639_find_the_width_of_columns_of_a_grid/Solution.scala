// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

object Solution {
  def findColumnWidth(grid: Array[Array[Int]]): Array[Int] = {
    val n = grid(0).length
    val ans = new Array[Int](n)
    var i = 0
    while (i < grid.length) {
      val row = grid(i)
      var j = 0
      while (j < n) {
        val w = width(row(j))
        if (w > ans(j)) ans(j) = w
        j += 1
      }
      i += 1
    }
    ans
  }

  private def width(x0: Int): Int = {
    if (x0 == 0) return 1
    var x = x0
    var w = 0
    if (x < 0) {
      w += 1
      x = -x
    }
    while (x > 0) {
      w += 1
      x /= 10
    }
    w
  }
}
