// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

object Solution {
  def uniquePaths(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = grid.length
    val n = grid(0).length

    def nextCell(i: Int, j: Int, di0: Int, dj0: Int): Array[Int] = {
      var di = di0
      var dj = dj0
      var ni = i + di
      var nj = j + dj
      while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid(ni)(nj) == 1) {
        if (dj == 1) {
          di = 1
          dj = 0
        } else {
          di = 0
          dj = 1
        }
        ni += di
        nj += dj
      }
      if (ni < 0 || nj < 0 || ni >= m || nj >= n) null
      else Array(ni, nj)
    }

    val dp = Array.ofDim[Int](m, n)
    if (grid(0)(0) == 1) return 0
    dp(0)(0) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(grid(i)(j) == 1 || dp(i)(j) == 0)) {
          val a = nextCell(i, j, 0, 1)
          if (a != null) dp(a(0))(a(1)) = (dp(a(0))(a(1)) + dp(i)(j)) % MOD
          val b = nextCell(i, j, 1, 0)
          if (b != null) dp(b(0))(b(1)) = (dp(b(0))(b(1)) + dp(i)(j)) % MOD
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)
  }
}
