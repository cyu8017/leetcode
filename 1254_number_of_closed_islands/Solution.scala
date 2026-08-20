// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

object Solution {
  def closedIsland(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    def flood(sr: Int, sc: Int): Boolean = {
      val stack = scala.collection.mutable.Stack((sr, sc))
      grid(sr)(sc) = 1
      var closed = true
      while (stack.nonEmpty) {
        val (r, c) = stack.pop()
        if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false
        for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) == 0) {
            grid(nr)(nc) = 1
            stack.push((nr, nc))
          }
        }
      }
      closed
    }
    var ans = 0
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 0) if (flood(r, c)) ans += 1
    ans
  }
}
