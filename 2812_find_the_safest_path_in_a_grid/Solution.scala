// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

object Solution {
  def maximumSafenessFactor(grid: List[List[Int]]): Int = {
    val n = grid.length
    val dist = Array.fill(n, n)(-1)
    val q = scala.collection.mutable.Queue.empty[(Int, Int)]
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          dist(i)(j) = 0
          q.enqueue((i, j))
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (q.nonEmpty) {
      val (x, y) = q.dequeue()
      dirs.foreach { case (dx, dy) =>
        val ni = x + dx
        val nj = y + dy
        if (ni >= 0 && nj >= 0 && ni < n && nj < n && dist(ni)(nj) == -1) {
          dist(ni)(nj) = dist(x)(y) + 1
          q.enqueue((ni, nj))
        }
      }
    }
    var lo = 0
    var hi = n * n
    var ans = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (ok(dist, dirs, mid)) {
        ans = mid
        lo = mid + 1
      } else hi = mid - 1
    }
    ans
  }

  private def ok(dist: Array[Array[Int]], dirs: Array[(Int, Int)], sf: Int): Boolean = {
    val n = dist.length
    if (dist(0)(0) < sf) return false
    val seen = Array.ofDim[Boolean](n, n)
    val st = scala.collection.mutable.ArrayBuffer((0, 0))
    seen(0)(0) = true
    while (st.nonEmpty) {
      val (x, y) = st.remove(st.length - 1)
      if (x == n - 1 && y == n - 1) return true
      dirs.foreach { case (dx, dy) =>
        val ni = x + dx
        val nj = y + dy
        if (ni >= 0 && nj >= 0 && ni < n && nj < n && !seen(ni)(nj) && dist(ni)(nj) >= sf) {
          seen(ni)(nj) = true
          st += ((ni, nj))
        }
      }
    }
    false
  }
}
