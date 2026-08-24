// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

object Solution {
  def countCells(grid: Array[Array[Char]], pattern: String): Int = {
    val m = grid.length
    val n = grid(0).length
    val row = new StringBuilder(m * n)
    val col = new StringBuilder(m * n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) { row.append(grid(i)(j)); j += 1 }
      i += 1
    }
    var j = 0
    while (j < n) {
      i = 0
      while (i < m) { col.append(grid(i)(j)); i += 1 }
      j += 1
    }
    val rowS = row.toString
    val colS = col.toString
    val hMark = Array.ofDim[Boolean](m, n)
    val vMark = Array.ofDim[Boolean](m, n)
    val plen = pattern.length
    i = 0
    while (i + plen <= rowS.length) {
      if (rowS.substring(i, i + plen) == pattern) {
        var t = 0
        while (t < plen) {
          val pos = i + t
          hMark(pos / n)(pos % n) = true
          t += 1
        }
      }
      i += 1
    }
    i = 0
    while (i + plen <= colS.length) {
      if (colS.substring(i, i + plen) == pattern) {
        var t = 0
        while (t < plen) {
          val pos = i + t
          vMark(pos % m)(pos / m) = true
          t += 1
        }
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < m) {
      j = 0
      while (j < n) {
        if (hMark(i)(j) && vMark(i)(j)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
