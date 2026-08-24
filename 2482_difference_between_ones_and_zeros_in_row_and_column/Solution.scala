// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

object Solution {
  def onesMinusZeros(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val row = new Array[Int](m)
    val col = new Array[Int](n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        row(i) += grid(i)(j)
        col(j) += grid(i)(j)
        j += 1
      }
      i += 1
    }
    val ans = Array.ofDim[Int](m, n)
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans(i)(j) = row(i) + col(j) - (m - row(i)) - (n - col(j))
        j += 1
      }
      i += 1
    }
    ans
  }
}
