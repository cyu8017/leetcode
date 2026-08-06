// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

object Solution {
  def maximumMinimumPath(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val pq = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)]
    pq.enqueue((grid(0)(0), 0, 0))
    val seen = Array.fill(m, n)(false)
    seen(0)(0) = true
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (pq.nonEmpty) {
      val (score, r, c) = pq.dequeue()
      if (r == m - 1 && c == n - 1) return score
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen(nr)(nc)) {
          seen(nr)(nc) = true
          pq.enqueue((math.min(score, grid(nr)(nc)), nr, nc))
        }
      }
    }
    grid(0)(0)
  }
}
