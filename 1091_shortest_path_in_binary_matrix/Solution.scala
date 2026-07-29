// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

object Solution {
  def shortestPathBinaryMatrix(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    if (grid(0)(0) != 0 || grid(n - 1)(n - 1) != 0) return -1
    val queue = scala.collection.mutable.Queue[(Int, Int, Int)]()
    queue.enqueue((0, 0, 1))
    grid(0)(0) = 1
    while (queue.nonEmpty) {
      val (r, c, dist) = queue.dequeue()
      if (r == n - 1 && c == n - 1) return dist
      for (dr <- -1 to 1; dc <- -1 to 1 if !(dr == 0 && dc == 0)) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid(nr)(nc) == 0) {
          grid(nr)(nc) = 1
          queue.enqueue((nr, nc, dist + 1))
        }
      }
    }
    -1
  }
}
