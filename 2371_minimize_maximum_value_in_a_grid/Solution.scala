// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

object Solution {
  def minScore(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val arr = Array.ofDim[Int](m * n, 3)
    var idx = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        arr(idx) = Array(grid(i)(j), i, j)
        idx += 1
        j += 1
      }
      i += 1
    }
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) => a(0) < b(0))
    val rowMax = Array.fill(m)(0)
    val colMax = Array.fill(n)(0)
    val ans = Array.ofDim[Int](m, n)
    arr.foreach { cel =>
      val v = math.max(rowMax(cel(1)), colMax(cel(2))) + 1
      ans(cel(1))(cel(2)) = v
      rowMax(cel(1)) = v
      colMax(cel(2)) = v
    }
    ans
  }
}
