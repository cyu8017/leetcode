// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

object Solution {
  def minimumTime(grid: Array[Array[Int]]): Int = {
    if (grid(0)(1) > 1 && grid(1)(0) > 1) return -1
    val m = grid.length
    val n = grid(0).length
    val dist = Array.fill(m, n)(1 << 30)
    val h = scala.collection.mutable.PriorityQueue.empty[Array[Int]](
      Ordering.by[Array[Int], Int](_(0)).reverse
    )
    h.enqueue(Array(0, 0, 0))
    dist(0)(0) = 0
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    while (h.nonEmpty) {
      val cur = h.dequeue()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      if (r == m - 1 && c == n - 1) return t
      if (t <= dist(r)(c)) {
        dirs.foreach { d =>
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
            var nt = t + 1
            if (nt < grid(nr)(nc)) {
              var wait = grid(nr)(nc) - nt
              if (wait % 2 == 1) wait += 1
              nt += wait
            }
            if (nt < dist(nr)(nc)) {
              dist(nr)(nc) = nt
              h.enqueue(Array(nt, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
