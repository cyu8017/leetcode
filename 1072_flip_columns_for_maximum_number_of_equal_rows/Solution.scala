// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

object Solution {
  def maxEqualRowsAfterFlips(matrix: Array[Array[Int]]): Int = {
    val patterns = scala.collection.mutable.Map.empty[String, Int].withDefaultValue(0)
    for (row <- matrix) {
      val base = row(0)
      val key = row.map(x => x ^ base).mkString(",")
      patterns(key) += 1
    }
    patterns.values.max
  }
}
