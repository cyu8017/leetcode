// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

object Solution {
  def minimumObstacles(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dist = Array.fill(m, n)(Int.MaxValue / 2)
    dist(0)(0) = 0
    val dq = scala.collection.mutable.ArrayDeque.empty[(Int, Int)]
    dq.append((0, 0))
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    while (dq.nonEmpty) {
      val (r, c) = dq.removeHead()
      for (d <- dirs) {
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val nd = dist(r)(c) + grid(nr)(nc)
          if (nd < dist(nr)(nc)) {
            dist(nr)(nc) = nd
            if (grid(nr)(nc) == 0) dq.prepend((nr, nc))
            else dq.append((nr, nc))
          }
        }
      }
    }
    dist(m - 1)(n - 1)
  }
}
