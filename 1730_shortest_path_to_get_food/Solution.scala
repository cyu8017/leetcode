// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

object Solution {
  def getFood(grid: Array[Array[Char]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val queue = scala.collection.mutable.Queue.empty[(Int, Int, Int)]
    val seen = Array.ofDim[Boolean](rows, cols)
    for (r <- 0 until rows; c <- 0 until cols) {
      if (grid(r)(c) == '*') {
        queue.enqueue((r, c, 0))
        seen(r)(c) = true
      }
    }
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (queue.nonEmpty) {
      val (r, c, d) = queue.dequeue()
      if (grid(r)(c) == '#') {
        return d
      }
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen(nr)(nc) && grid(nr)(nc) != 'X') {
          seen(nr)(nc) = true
          queue.enqueue((nr, nc, d + 1))
        }
      }
    }
    -1
  }
}
