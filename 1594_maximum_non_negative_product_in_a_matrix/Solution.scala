// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

object Solution {
  def maxProductPath(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    val m = grid.length
    val n = grid(0).length
    val high = Array.fill(m, n)(0L)
    val low = Array.fill(m, n)(0L)
    high(0)(0) = grid(0)(0)
    low(0)(0) = grid(0)(0)
    for (r <- 0 until m; c <- 0 until n if !(r == 0 && c == 0)) {
      val values = scala.collection.mutable.ArrayBuffer.empty[Long]
      if (r > 0) {
        values += high(r - 1)(c) * grid(r)(c)
        values += low(r - 1)(c) * grid(r)(c)
      }
      if (c > 0) {
        values += high(r)(c - 1) * grid(r)(c)
        values += low(r)(c - 1) * grid(r)(c)
      }
      high(r)(c) = values.max
      low(r)(c) = values.min
    }
    if (high(m - 1)(n - 1) >= 0) (high(m - 1)(n - 1) % MOD).toInt else -1
  }
}
