// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

object Solution {
  def matrixSumQueries(n: Int, queries: Array[Array[Int]]): Long = {
    val rowDone = new Array[Boolean](n)
    val colDone = new Array[Boolean](n)
    var rowsLeft = n
    var colsLeft = n
    var ans = 0L
    var i = queries.length - 1
    while (i >= 0) {
      val typ = queries(i)(0)
      val idx = queries(i)(1)
      val v = queries(i)(2)
      if (typ == 0) {
        if (!rowDone(idx)) {
          ans += v.toLong * colsLeft
          rowDone(idx) = true
          rowsLeft -= 1
        }
      } else if (!colDone(idx)) {
        ans += v.toLong * rowsLeft
        colDone(idx) = true
        colsLeft -= 1
      }
      i -= 1
    }
    ans
  }
}
