// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

object Solution {
  def maxPoints(grid: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val order = Array.tabulate(queries.length)(identity)
    scala.util.Sorting.stableSort(order, (a: Int, b: Int) => queries(a) < queries(b) || (queries(a) == queries(b) && a < b))
    val ans = new Array[Int](queries.length)
    val visited = Array.ofDim[Boolean](m, n)
    implicit val ord: Ordering[(Int, Int, Int)] = Ordering.by[(Int, Int, Int), Int](_._1).reverse
    val pq = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)]
    pq.enqueue((grid(0)(0), 0, 0))
    visited(0)(0) = true
    var points = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    var oi = 0
    while (oi < order.length) {
      val qi = order(oi)
      val q = queries(qi)
      while (pq.nonEmpty && pq.head._1 < q) {
        val (_, r, c) = pq.dequeue()
        points += 1
        var d = 0
        while (d < 4) {
          val nr = r + dirs(d)._1
          val nc = c + dirs(d)._2
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc)) {
            visited(nr)(nc) = true
            pq.enqueue((grid(nr)(nc), nr, nc))
          }
          d += 1
        }
      }
      ans(qi) = points
      oi += 1
    }
    ans
  }
}
