// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

object Solution {
  def orangesRotting(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val q = scala.collection.mutable.Queue.empty[(Int, Int)]
    var fresh = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 2) q.enqueue((i, j))
        else if (grid(i)(j) == 1) fresh += 1
        j += 1
      }
      i += 1
    }
    var minutes = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (q.nonEmpty && fresh > 0) {
      val sz = q.size
      var s = 0
      while (s < sz) {
        val (r, c) = q.dequeue()
        dirs.foreach { case (dr, dc) =>
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) == 1) {
            grid(nr)(nc) = 2
            fresh -= 1
            q.enqueue((nr, nc))
          }
        }
        s += 1
      }
      minutes += 1
    }
    if (fresh == 0) minutes else -1
  }
}
