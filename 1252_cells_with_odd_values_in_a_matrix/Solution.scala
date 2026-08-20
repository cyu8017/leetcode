// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

object Solution {
  def oddCells(m: Int, n: Int, indices: Array[Array[Int]]): Int = {
    val rows = Array.fill(m)(0)
    val cols = Array.fill(n)(0)
    for (idx <- indices) {
      rows(idx(0)) ^= 1
      cols(idx(1)) ^= 1
    }
    (for (r <- 0 until m; c <- 0 until n if (rows(r) ^ cols(c)) == 1) yield 1).sum
  }
}
