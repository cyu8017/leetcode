// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val dist = Array.fill(m, n)(1 << 30)
    val h = new java.util.PriorityQueue[Array[Int]]((a, b) => Integer.compare(a(0), b(0)))
    h.offer(Array(0, 0, 0))
    dist(0)(0) = 0
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!h.isEmpty) {
      val cur = h.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      if (t == dist(r)(c)) {
        if (r == m - 1 && c == n - 1) return t
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + 1
            if (nt < dist(nr)(nc)) {
              dist(nr)(nc) = nt
              h.offer(Array(nt, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
