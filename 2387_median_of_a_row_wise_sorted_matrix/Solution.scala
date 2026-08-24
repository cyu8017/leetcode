// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

object Solution {
  def matrixMedian(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var lo = 1
    var hi = 1000000
    val need = (m * n) / 2 + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (countLE(grid, mid, n) >= need) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def countLE(grid: Array[Array[Int]], x: Int, n: Int): Int = {
    var cnt = 0
    grid.foreach { row =>
      var l = 0
      var r = n
      while (l < r) {
        val mid = (l + r) / 2
        if (row(mid) <= x) l = mid + 1
        else r = mid
      }
      cnt += l
    }
    cnt
  }
}
