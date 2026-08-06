// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

object Solution {
  def containsCycle(grid: Array[Array[Char]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val seen = scala.collection.mutable.Set.empty[(Int, Int)]
    def dfs(r: Int, c: Int, pr: Int, pc: Int): Boolean = {
      seen += ((r, c))
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) == grid(r)(c) && !(nr == pr && nc == pc)) {
          if (seen.contains((nr, nc)) || dfs(nr, nc, r, c)) return true
        }
      }
      false
    }
    for (r <- 0 until m; c <- 0 until n if !seen.contains((r, c))) {
      if (dfs(r, c, -1, -1)) return true
    }
    false
  }
}
