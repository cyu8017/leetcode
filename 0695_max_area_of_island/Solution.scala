// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

object Solution {
  def maxAreaOfIsland(grid: Array[Array[Int]]): Int = {
    def dfs(r: Int, c: Int): Int = {
      if (r < 0 || r >= grid.length || c < 0 || c >= grid(0).length || grid(r)(c) == 0) return 0
      grid(r)(c) = 0
      1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    }
    var best = 0
    var i = 0
    while (i < grid.length) {
      var j = 0
      while (j < grid(0).length) {
        best = math.max(best, dfs(i, j))
        j += 1
      }
      i += 1
    }
    best
  }
}
