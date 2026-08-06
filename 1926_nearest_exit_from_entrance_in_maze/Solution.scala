// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

object Solution {
  def nearestExit(maze: Array[Array[Char]], entrance: Array[Int]): Int = {
    val m = maze.length
    val n = maze(0).length
    val er = entrance(0)
    val ec = entrance(1)
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((er, ec, 0))
    maze(er)(ec) = '+'
    while (q.nonEmpty) {
      val (r, c, d) = q.dequeue()
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && maze(nr)(nc) == '.') {
          if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) return d + 1
          maze(nr)(nc) = '+'
          q.enqueue((nr, nc, d + 1))
        }
      }
    }
    -1
  }
}
