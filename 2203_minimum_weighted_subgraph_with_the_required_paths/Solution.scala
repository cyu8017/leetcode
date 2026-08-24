// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

object Solution {
  def minimumWeight(n: Int, edges: Array[Array[Int]], src1: Int, src2: Int, dest: Int): Long = {
    val INF = 1L << 62
    def dijkstra(g: Array[List[(Int, Int)]], src: Int): Array[Long] = {
      val dist = Array.fill(n)(INF)
      dist(src) = 0L
      val pq = scala.collection.mutable.PriorityQueue.empty[(Long, Int)](
        Ordering.by[(Long, Int), Long](_._1).reverse
      )
      pq.enqueue((0L, src))
      while (pq.nonEmpty) {
        val (d, u) = pq.dequeue()
        if (d == dist(u)) {
          for ((v, w) <- g(u)) {
            if (d + w < dist(v)) {
              dist(v) = d + w
              pq.enqueue((dist(v), v))
            }
          }
        }
      }
      dist
    }
    val g = Array.fill(n)(List.empty[(Int, Int)])
    val rg = Array.fill(n)(List.empty[(Int, Int)])
    for (e <- edges) {
      g(e(0)) = (e(1), e(2)) :: g(e(0))
      rg(e(1)) = (e(0), e(2)) :: rg(e(1))
    }
    val d1 = dijkstra(g, src1)
    val d2 = dijkstra(g, src2)
    val dd = dijkstra(rg, dest)
    var ans = INF
    var i = 0
    while (i < n) {
      if (d1(i) < INF && d2(i) < INF && dd(i) < INF) {
        ans = math.min(ans, d1(i) + d2(i) + dd(i))
      }
      i += 1
    }
    if (ans >= INF) -1L else ans
  }
}
