// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

object Solution {
  def findSafeWalk(grid: Array[Array[Int]], health: Int): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val vis = Array.fill(m, n)(-1)
    val qh = health - grid(0)(0)
    if (qh <= 0) return false
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((0, 0, qh))
    vis(0)(0) = qh
    val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))
    while (q.nonEmpty) {
      val (r, c, h) = q.dequeue()
      if (r == m - 1 && c == n - 1) return true
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
          val nh = h - grid(nr)(nc)
          if (nh > 0 && nh > vis(nr)(nc)) {
            vis(nr)(nc) = nh
            q.enqueue((nr, nc, nh))
          }
        }
      }
    }
    false
  }
}
