// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

object Solution {
  def constructProductMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val mod = 12345
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m, n)
    var pref = 1
    for (i <- 0 until m; j <- 0 until n) {
      ans(i)(j) = pref
      pref = (1L * pref * (grid(i)(j) % mod) % mod).toInt
    }
    var suf = 1
    for (i <- m - 1 to 0 by -1; j <- n - 1 to 0 by -1) {
      ans(i)(j) = (1L * ans(i)(j) * suf % mod).toInt
      suf = (1L * suf * (grid(i)(j) % mod) % mod).toInt
    }
    ans
  }
}
