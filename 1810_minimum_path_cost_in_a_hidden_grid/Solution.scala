// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

object Solution {
  // Test harness passes the revealed grid plus start/target coordinates.
  def findShortestPath(grid: Array[Array[Int]], r1: Int, c1: Int, r2: Int, c2: Int): Int = {
    if (r1 == r2 && c1 == c2) return 0
    val m = grid.length
    val n = grid(0).length
    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))
    val dist = Array.fill(m, n)(Int.MaxValue)
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)](
      Ordering.by[(Int, Int, Int), Int](_._1).reverse
    )
    dist(r1)(c1) = 0
    heap.enqueue((0, r1, c1))

    while (heap.nonEmpty) {
      val (d, r, c) = heap.dequeue()
      if (r == r2 && c == c2) return d
      if (d <= dist(r)(c)) {
        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 0) {
            val nd = d + grid(nr)(nc)
            if (nd < dist(nr)(nc)) {
              dist(nr)(nc) = nd
              heap.enqueue((nd, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
