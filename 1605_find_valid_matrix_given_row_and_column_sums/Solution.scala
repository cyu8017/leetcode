// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

object Solution {
  def restoreMatrix(rowSum: Array[Int], colSum: Array[Int]): Array[Array[Int]] = {
    val rs = rowSum.clone()
    val cs = colSum.clone()
    val ans = Array.ofDim[Int](rs.length, cs.length)
    var i = 0
    var j = 0
    while (i < rs.length && j < cs.length) {
      val x = math.min(rs(i), cs(j))
      ans(i)(j) = x
      rs(i) -= x
      cs(j) -= x
      if (rs(i) == 0) i += 1
      if (cs(j) == 0) j += 1
    }
    ans
  }
}
