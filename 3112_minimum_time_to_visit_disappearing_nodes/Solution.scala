// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

object Solution {
  def minimumTime(n: Int, edges: Array[Array[Int]], disappear: Array[Int]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }
    val INF = 1 << 30
    val dist = Array.fill(n)(INF)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => a(0) - b(0))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val du = cur(0)
      val u = cur(1)
      if (du <= dist(u)) {
        g(u).foreach { e =>
          val v = e(0)
          val w = e(1)
          if (dist(v) > dist(u) + w && dist(u) + w < disappear(v)) {
            dist(v) = dist(u) + w
            pq.offer(Array(dist(v), v))
          }
        }
      }
    }
    Array.tabulate(n)(i => if (dist(i) < disappear(i)) dist(i) else -1)
  }
}
