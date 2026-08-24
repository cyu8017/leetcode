// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val INF = 1 << 30
    val dist = Array.fill(m, n, 2)(INF)
    val pq = new java.util.PriorityQueue[Array[Int]]((a, b) => Integer.compare(a(0), b(0)))
    dist(0)(0)(0) = 0
    pq.offer(Array(0, 0, 0, 0))
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      val parity = cur(3)
      if (t == dist(r)(c)(parity)) {
        if (r == m - 1 && c == n - 1) return t
        val cost = if (parity == 1) 2 else 1
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + cost
            val np = 1 - parity
            if (nt < dist(nr)(nc)(np)) {
              dist(nr)(nc)(np) = nt
              pq.offer(Array(nt, nr, nc, np))
            }
          }
        }
      }
    }
    -1
  }
}
