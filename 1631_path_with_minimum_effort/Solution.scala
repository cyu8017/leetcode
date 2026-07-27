// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

import scala.collection.mutable

object Solution {
  def minimumEffortPath(heights: Array[Array[Int]]): Int = {
    val m = heights.length
    val n = heights(0).length
    val dist = Array.fill(m, n)(Int.MaxValue)
    dist(0)(0) = 0
    val heap = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](_._1).reverse)
    heap.enqueue((0, 0, 0))
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (heap.nonEmpty) {
      val (effort, i, j) = heap.dequeue()
      if (i == m - 1 && j == n - 1) return effort
      if (effort == dist(i)(j)) {
        for ((di, dj) <- dirs) {
          val x = i + di
          val y = j + dj
          if (x >= 0 && x < m && y >= 0 && y < n) {
            val nd = math.max(effort, math.abs(heights(i)(j) - heights(x)(y)))
            if (nd < dist(x)(y)) {
              dist(x)(y) = nd
              heap.enqueue((nd, x, y))
            }
          }
        }
      }
    }
    0
  }
}
