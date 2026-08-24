// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

object Solution {
  def networkBecomesIdle(edges: Array[Array[Int]], patience: Array[Int]): Int = {
    val n = patience.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e => g(e(0)) += e(1); g(e(1)) += e(0) }
    val dist = Array.fill(n)(-1)
    val q = scala.collection.mutable.Queue(0)
    dist(0) = 0
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).foreach { v =>
        if (dist(v) == -1) { dist(v) = dist(u) + 1; q.enqueue(v) }
      }
    }
    var ans = 0
    var i = 1
    while (i < n) {
      val round = dist(i) * 2
      val lastSend = (round - 1) / patience(i) * patience(i)
      ans = math.max(ans, lastSend + round)
      i += 1
    }
    ans + 1
  }
}
