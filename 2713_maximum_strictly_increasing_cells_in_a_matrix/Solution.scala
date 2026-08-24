// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

object Solution {
  def maxIncreasingCells(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val cells = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        cells += Array(mat(i)(j), i, j)
        j += 1
      }
      i += 1
    }
    val sorted = cells.sortBy(_(0))
    val rowMax = new Array[Int](m)
    val colMax = new Array[Int](n)
    val dp = Array.ofDim[Int](m, n)
    var ans = 0
    i = 0
    while (i < sorted.length) {
      var j = i
      while (j < sorted.length && sorted(j)(0) == sorted(i)(0)) j += 1
      val buf = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
      var k = i
      while (k < j) {
        val r = sorted(k)(1)
        val c = sorted(k)(2)
        val best = math.max(rowMax(r), colMax(c))
        dp(r)(c) = best + 1
        ans = math.max(ans, dp(r)(c))
        buf += Array(r, c, dp(r)(c))
        k += 1
      }
      buf.foreach { b =>
        rowMax(b(0)) = math.max(rowMax(b(0)), b(2))
        colMax(b(1)) = math.max(colMax(b(1)), b(2))
      }
      i = j
    }
    ans
  }
}
