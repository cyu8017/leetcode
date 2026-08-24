// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

object Solution {
  def maximumRows(matrix: Array[Array[Int]], numSelect: Int): Int = {
    val m = matrix.length
    val n = matrix(0).length
    var ans = 0

    def dfs(col: Int, chosen: Int, mask: Int): Unit = {
      if (chosen == numSelect) {
        var covered = 0
        var i = 0
        while (i < m) {
          var ok = true
          var j = 0
          while (j < n && ok) {
            if (matrix(i)(j) == 1 && ((mask >> j) & 1) == 0) ok = false
            j += 1
          }
          if (ok) covered += 1
          i += 1
        }
        ans = math.max(ans, covered)
        return
      }
      if (col == n) return
      dfs(col + 1, chosen + 1, mask | (1 << col))
      dfs(col + 1, chosen, mask)
    }

    dfs(0, 0, 0)
    ans
  }
}
