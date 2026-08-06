// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

object Solution {
  def maxDistance(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    for (r <- 0 until n; c <- 0 until n if grid(r)(c) == 1) q.enqueue((r, c))
    if (q.isEmpty || q.size == n * n) return -1
    var dist = -1
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (q.nonEmpty) {
      dist += 1
      val size = q.size
      for (_ <- 0 until size) {
        val (r, c) = q.dequeue()
        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid(nr)(nc) == 0) {
            grid(nr)(nc) = 1
            q.enqueue((nr, nc))
          }
        }
      }
    }
    dist
  }
}
