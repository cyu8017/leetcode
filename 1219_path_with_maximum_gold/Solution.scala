// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

object Solution {
  def getMaximumGold(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    def dfs(r: Int, c: Int): Int = {
      val gold = grid(r)(c)
      grid(r)(c) = 0
      var best = 0
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid(nr)(nc) > 0) {
          best = math.max(best, dfs(nr, nc))
        }
      }
      grid(r)(c) = gold
      gold + best
    }
    var ans = 0
    for (r <- 0 until rows; c <- 0 until cols if grid(r)(c) > 0) ans = math.max(ans, dfs(r, c))
    ans
  }
}
