// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

object Solution {
  def maxMatrixSum(matrix: Array[Array[Int]]): Long = {
    var total = 0L
    var neg = 0
    var mn = Long.MaxValue
    for (row <- matrix; x <- row) {
      if (x < 0) neg += 1
      val ax = math.abs(x.toLong)
      total += ax
      mn = math.min(mn, ax)
    }
    if (neg % 2 == 0) total else total - 2 * mn
  }
}
