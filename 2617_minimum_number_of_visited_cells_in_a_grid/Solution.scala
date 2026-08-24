// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

object Solution {
  def minimumVisitedCells(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dist = Array.fill(m, n)(-1)
    val q = scala.collection.mutable.Queue[Array[Int]]()
    q.enqueue(Array(0, 0))
    dist(0)(0) = 1
    while (q.nonEmpty) {
      val cur = q.dequeue()
      val r = cur(0)
      val c = cur(1)
      if (r == m - 1 && c == n - 1) return dist(r)(c)
      var nc = c + 1
      while (nc <= c + grid(r)(c) && nc < n) {
        if (dist(r)(nc) == -1) {
          dist(r)(nc) = dist(r)(c) + 1
          q.enqueue(Array(r, nc))
        }
        nc += 1
      }
      var nr = r + 1
      while (nr <= r + grid(r)(c) && nr < m) {
        if (dist(nr)(c) == -1) {
          dist(nr)(c) = dist(r)(c) + 1
          q.enqueue(Array(nr, c))
        }
        nr += 1
      }
    }
    -1
  }
}
