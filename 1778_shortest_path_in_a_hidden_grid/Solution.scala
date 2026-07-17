// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

object Solution {
  def findShortestPath(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var sr = 0
    var sc = 0
    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) == -1) {
        sr = i
        sc = j
      }
    }
    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))
    val dist = Array.fill(m, n)(-1)
    val queue = scala.collection.mutable.Queue.empty[(Int, Int)]
    dist(sr)(sc) = 0
    queue.enqueue((sr, sc))
    while (queue.nonEmpty) {
      val (r, c) = queue.dequeue()
      if (grid(r)(c) == 2) {
        return dist(r)(c)
      }
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 0 && dist(nr)(nc) < 0) {
          dist(nr)(nc) = dist(r)(c) + 1
          queue.enqueue((nr, nc))
        }
      }
    }
    -1
  }
}
