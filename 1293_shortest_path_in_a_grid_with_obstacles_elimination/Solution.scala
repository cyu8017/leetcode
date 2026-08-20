// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

object Solution {
  def shortestPath(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    if (k >= m + n - 2) return m + n - 2
    val q = scala.collection.mutable.Queue((0, 0, k, 0))
    val best = scala.collection.mutable.Map((0, 0) -> k)
    while (q.nonEmpty) {
      val (r, c, remaining, distance) = q.dequeue()
      if (r == m - 1 && c == n - 1) return distance
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val nxt = remaining - grid(nr)(nc)
          if (nxt >= 0 && nxt > best.getOrElse((nr, nc), -1)) {
            best((nr, nc)) = nxt
            q.enqueue((nr, nc, nxt, distance + 1))
          }
        }
      }
    }
    -1
  }
}
