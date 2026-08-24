// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

object Solution {
  def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
    val diff = Array.fill(n + 1, n + 1)(0)
    queries.foreach { q =>
      val r1 = q(0)
      val c1 = q(1)
      val r2 = q(2)
      val c2 = q(3)
      diff(r1)(c1) += 1
      diff(r1)(c2 + 1) -= 1
      diff(r2 + 1)(c1) -= 1
      diff(r2 + 1)(c2 + 1) += 1
    }
    val mat = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        var v = diff(i)(j)
        if (i > 0) v += mat(i - 1)(j)
        if (j > 0) v += mat(i)(j - 1)
        if (i > 0 && j > 0) v -= mat(i - 1)(j - 1)
        mat(i)(j) = v
        j += 1
      }
      i += 1
    }
    mat
  }
}
