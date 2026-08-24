// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

object Solution {
  def shortestBridge(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    def dfs(r: Int, c: Int): Unit = {
      if (r < 0 || r >= n || c < 0 || c >= n || grid(r)(c) != 1) return
      grid(r)(c) = 2
      dirs.foreach { d => dfs(r + d(0), c + d(1)) }
    }
    var found = false
    var i = 0
    while (i < n && !found) {
      var j = 0
      while (j < n && !found) {
        if (grid(i)(j) == 1) { dfs(i, j); found = true }
        j += 1
      }
      i += 1
    }
    val q = scala.collection.mutable.Queue[Array[Int]]()
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 2) q.enqueue(Array(i, j, 0))
        j += 1
      }
      i += 1
    }
    while (q.nonEmpty) {
      val cur = q.dequeue()
      val r = cur(0)
      val c = cur(1)
      val dist = cur(2)
      dirs.foreach { d =>
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
          if (grid(nr)(nc) == 1) return dist
          if (grid(nr)(nc) == 0) {
            grid(nr)(nc) = 2
            q.enqueue(Array(nr, nc, dist + 1))
          }
        }
      }
    }
    -1
  }
}
