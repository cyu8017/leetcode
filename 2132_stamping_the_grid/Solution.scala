// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

object Solution {
  def possibleToStamp(grid: Array[Array[Int]], stampHeight: Int, stampWidth: Int): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val pref = Array.fill(m + 1, n + 1)(0)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        pref(i + 1)(j + 1) = pref(i + 1)(j) + pref(i)(j + 1) - pref(i)(j) + grid(i)(j)
        j += 1
      }
      i += 1
    }
    val diff = Array.fill(m + 1, n + 1)(0)
    i = 0
    while (i + stampHeight - 1 < m) {
      var j = 0
      while (j + stampWidth - 1 < n) {
        val sum = pref(i + stampHeight)(j + stampWidth) - pref(i)(j + stampWidth) - pref(i + stampHeight)(j) + pref(i)(j)
        if (sum == 0) {
          diff(i)(j) += 1
          diff(i)(j + stampWidth) -= 1
          diff(i + stampHeight)(j) -= 1
          diff(i + stampHeight)(j + stampWidth) += 1
        }
        j += 1
      }
      i += 1
    }
    val cur = Array.fill(m, n)(0)
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var v = diff(i)(j)
        if (i > 0) v += cur(i - 1)(j)
        if (j > 0) v += cur(i)(j - 1)
        if (i > 0 && j > 0) v -= cur(i - 1)(j - 1)
        cur(i)(j) = v
        if (grid(i)(j) == 0 && v == 0) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
