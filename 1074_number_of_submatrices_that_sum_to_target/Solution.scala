// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

object Solution {
  def numSubmatrixSumTarget(matrix: Array[Array[Int]], target: Int): Int = {
    val rows = matrix.length
    val cols = matrix(0).length
    var ans = 0
    for (left <- 0 until cols) {
      val rowSum = Array.fill(rows)(0)
      for (right <- left until cols) {
        for (r <- 0 until rows) rowSum(r) += matrix(r)(right)
        var prefix = 0
        val seen = scala.collection.mutable.Map(0 -> 1)
        for (v <- rowSum) {
          prefix += v
          ans += seen.getOrElse(prefix - target, 0)
          seen(prefix) = seen.getOrElse(prefix, 0) + 1
        }
      }
    }
    ans
  }
}
