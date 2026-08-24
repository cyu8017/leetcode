// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

import scala.collection.mutable

object Solution {
  def minCost(m: Int, n: Int, penalty: Array[Array[Int]]): Long = {
    val INF = 1L << 60
    val dist = Array.fill(m, n, 2)(INF)
    dist(0)(0)(1) = 1
    val pq = mutable.PriorityQueue.empty[(Long, Int, Int, Int)](Ordering.by[(Long, Int, Int, Int), Long](_._1).reverse)
    pq.enqueue((1L, 0, 0, 1))
    val dirs = Array(Array(-1, 0), Array(0, 1), Array(0, -1), Array(1, 0))
    while (pq.nonEmpty) {
      val (d, i, j, k) = pq.dequeue()
      if (i == m - 1 && j == n - 1) return d
      if (d <= dist(i)(j)(k)) {
        val p = penalty(i)(j)
        var nd = d + p
        if (nd < dist(i)(j)(k ^ 1)) {
          dist(i)(j)(k ^ 1) = nd
          pq.enqueue((nd, i, j, k ^ 1))
        }
        var idx = 0
        while (idx < 4) {
          val x = i + dirs(idx)(0)
          val y = j + dirs(idx)(1)
          if (0 <= x && x < m && 0 <= y && y < n) {
            nd = d + ((x + 1).toLong * (y + 1) + (((idx & 1) ^ k) * p))
            if (nd < dist(x)(y)(k ^ 1)) {
              dist(x)(y)(k ^ 1) = nd
              pq.enqueue((nd, x, y, k ^ 1))
            }
          }
          idx += 1
        }
      }
    }
    -1
  }
}
