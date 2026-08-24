// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

object Solution {
  def maximumMinutes(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val inf = 1000000000
    val fire = Array.fill(m, n)(inf)
    val q = scala.collection.mutable.Queue.empty[(Int, Int)]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          fire(i)(j) = 0
          q.enqueue((i, j))
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    while (q.nonEmpty) {
      val (r, c) = q.dequeue()
      for (d <- dirs) {
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 2 && fire(nr)(nc) == inf) {
          fire(nr)(nc) = fire(r)(c) + 1
          q.enqueue((nr, nc))
        }
      }
    }
    def can(wait: Int): Boolean = {
      if (wait >= fire(0)(0)) return false
      val vis = Array.fill(m, n)(false)
      val qq = scala.collection.mutable.Queue.empty[(Int, Int, Int)]
      qq.enqueue((0, 0, wait))
      vis(0)(0) = true
      while (qq.nonEmpty) {
        val (r, c, t) = qq.dequeue()
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          val nt = t + 1
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 2 && !vis(nr)(nc)) {
            if (nr == m - 1 && nc == n - 1) {
              if (nt <= fire(nr)(nc)) return true
            } else if (nt < fire(nr)(nc)) {
              vis(nr)(nc) = true
              qq.enqueue((nr, nc, nt))
            }
          }
        }
      }
      false
    }
    var lo = 0
    var hi = m * n + 10
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (can(mid)) {
        ans = mid
        lo = mid + 1
      } else hi = mid - 1
    }
    if (ans >= m * n) inf else ans
  }
}
