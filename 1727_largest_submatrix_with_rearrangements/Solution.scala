// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

object Solution {
  def largestSubmatrix(matrix: Array[Array[Int]]): Int = {
    val m = matrix.length
    val n = matrix(0).length
    val heights = new Array[Int](n)
    var best = 0
    for (r <- 0 until m) {
      for (c <- 0 until n) {
        heights(c) = if (matrix(r)(c) == 1) heights(c) + 1 else 0
      }
      val sorted = heights.sorted(Ordering.Int.reverse)
      for (width <- 1 to n) {
        best = math.max(best, width * sorted(width - 1))
      }
    }
    best
  }
}
