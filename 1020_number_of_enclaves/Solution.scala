// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

object Solution {
  def numEnclaves(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    def dfs(r: Int, c: Int): Unit = {
      if (r < 0 || r >= m || c < 0 || c >= n || grid(r)(c) != 1) return
      grid(r)(c) = 0
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)
    }
    for (i <- 0 until m) {
      dfs(i, 0)
      dfs(i, n - 1)
    }
    for (j <- 0 until n) {
      dfs(0, j)
      dfs(m - 1, j)
    }
    grid.map(_.sum).sum
  }
}
