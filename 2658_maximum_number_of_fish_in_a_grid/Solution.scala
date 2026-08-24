// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

object Solution {
  def findMaxFish(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var best = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) > 0) best = math.max(best, dfs(grid, i, j))
        j += 1
      }
      i += 1
    }
    best
  }

  private def dfs(grid: Array[Array[Int]], r: Int, c: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    if (r < 0 || r >= m || c < 0 || c >= n || grid(r)(c) == 0) return 0
    val fish = grid(r)(c)
    grid(r)(c) = 0
    fish + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
  }
}
