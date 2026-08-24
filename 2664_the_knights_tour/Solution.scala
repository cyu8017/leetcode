// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

object Solution {
  private val DIRS = Array(
    Array(1, 2), Array(1, -2), Array(-1, 2), Array(-1, -2),
    Array(2, 1), Array(2, -1), Array(-2, 1), Array(-2, -1)
  )

  def tourOfKnight(m: Int, n: Int, r: Int, c: Int): Array[Array[Int]] = {
    val ans = Array.fill(m, n)(-1)
    dfs(ans, m, n, r, c, 0)
    ans
  }

  private def dfs(ans: Array[Array[Int]], m: Int, n: Int, x: Int, y: Int, step: Int): Boolean = {
    ans(x)(y) = step
    if (step == m * n - 1) return true
    var i = 0
    while (i < DIRS.length) {
      val nx = x + DIRS(i)(0)
      val ny = y + DIRS(i)(1)
      if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans(nx)(ny) == -1)
        if (dfs(ans, m, n, nx, ny, step + 1)) return true
      i += 1
    }
    ans(x)(y) = -1
    false
  }
}
