// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

object Solution {
  def findMaxPathScore(edges: Array[Array[Int]], online: Array[Boolean], k: Long): Int = {
    val n = online.length
    val g = Array.fill[java.util.List[Array[Int]]](n)(new java.util.ArrayList[Array[Int]]())
    var l = Int.MaxValue
    var r = 0
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      val w = e(2)
      if (online(u) && online(v)) {
        g(u).add(Array(v, w))
        l = math.min(l, w)
        r = math.max(r, w)
      }
    }
    if (l == Int.MaxValue) return -1

    def check(mid: Int): Boolean = {
      val INF = Int.MaxValue / 2
      val dist = Array.fill(n)(INF)
      dist(0) = 0
      val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
      pq.offer(Array(0, 0))
      while (!pq.isEmpty) {
        val cur = pq.poll()
        val d = cur(0)
        val u = cur(1)
        if (d.toLong > k) return false
        if (u == n - 1) return true
        if (dist(u) >= d) {
          val it = g(u).iterator()
          while (it.hasNext) {
            val e = it.next()
            val v = e(0)
            val w = e(1)
            if (w >= mid) {
              val nd = d + w
              if (nd < dist(v)) {
                dist(v) = nd
                pq.offer(Array(nd, v))
              }
            }
          }
        }
      }
      false
    }

    while (l < r) {
      val mid = (l + r + 1) >> 1
      if (check(mid)) l = mid
      else r = mid - 1
    }
    if (check(l)) l else -1
  }
}
