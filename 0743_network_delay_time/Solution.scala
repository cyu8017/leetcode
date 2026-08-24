// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

object Solution {
  def networkDelayTime(times: Array[Array[Int]], n: Int, k: Int): Int = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    for (edge <- times) graph(edge(0)) += Array(edge(1), edge(2))
    val INF = Int.MaxValue / 4
    val dist = Array.fill(n + 1)(INF)
    dist(k) = 0
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)
    heap.enqueue((0, k))
    while (heap.nonEmpty) {
      val (d, node) = heap.dequeue()
      if (d <= dist(node)) {
        for (e <- graph(node)) {
          val nd = d + e(1)
          if (nd < dist(e(0))) {
            dist(e(0)) = nd
            heap.enqueue((nd, e(0)))
          }
        }
      }
    }
    var ans = 0
    var i = 1
    while (i <= n) {
      ans = math.max(ans, dist(i))
      i += 1
    }
    if (ans == INF) -1 else ans
  }
}
