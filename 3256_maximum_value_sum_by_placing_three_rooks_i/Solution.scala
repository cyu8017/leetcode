// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

object Solution {
  class Cell(var v: Int, var c: Int)
  def maximumValueSum(board: Array[Array[Int]]): Long = {
    val m = board.length
    val n = board(0).length
    val tops = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Cell]]
    var i = 0
    while (i < m) {
      val row = scala.collection.mutable.ArrayBuffer.empty[Cell]
      var j = 0
      while (j < n) {
        val cur = new Cell(board(i)(j), j)
        var placed = false
        var t = 0
        while (t < row.length && !placed) {
          if (cur.v > row(t).v) { row.insert(t, cur); placed = true }
          t += 1
        }
        if (!placed) row += cur
        if (row.length > 3) row.remove(3, row.length - 3)
        j += 1
      }
      tops += row
      i += 1
    }
    var ans = -(1L << 62)
    i = 0
    while (i < m) {
      for (a <- tops(i)) {
        var j = i + 1
        while (j < m) {
          for (b <- tops(j) if a.c != b.c) {
            var k = j + 1
            while (k < m) {
              for (c <- tops(k) if c.c != a.c && c.c != b.c) {
                val s = a.v.toLong + b.v + c.v
                if (s > ans) ans = s
              }
              k += 1
            }
          }
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
