// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

import scala.collection.mutable

object Solution {
  def minimumCost(start: Array[Int], target: Array[Int], specialRoads: Array[Array[Int]]): Int = {
    val points = mutable.ArrayBuffer.empty[Array[Int]]
    points += start
    points += target
    var i = 0
    while (i < specialRoads.length) {
      val r = specialRoads(i)
      points += Array(r(0), r(1))
      points += Array(r(2), r(3))
      i += 1
    }
    val N = points.length
    val g = Array.fill(N)(mutable.ArrayBuffer.empty[Array[Int]])
    i = 0
    while (i < N) {
      var j = 0
      while (j < N) {
        if (i != j) g(i) += Array(j, man(points(i), points(j)))
        j += 1
      }
      i += 1
    }
    i = 0
    while (i < specialRoads.length) {
      val r = specialRoads(i)
      var u = -1
      var v = -1
      var k = 0
      while (k < N) {
        val p = points(k)
        if (p(0) == r(0) && p(1) == r(1)) u = k
        if (p(0) == r(2) && p(1) == r(3)) v = k
        k += 1
      }
      if (u >= 0 && v >= 0) g(u) += Array(v, r(4))
      i += 1
    }
    val dist = Array.fill(N)(Int.MaxValue / 4)
    dist(0) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((0, 0))
    while (pq.nonEmpty) {
      val (id, cost) = pq.dequeue()
      if (cost <= dist(id)) {
        g(id).foreach { e =>
          if (cost + e(1) < dist(e(0))) {
            dist(e(0)) = cost + e(1)
            pq.enqueue((e(0), dist(e(0))))
          }
        }
      }
    }
    dist(1)
  }

  private def man(a: Array[Int], b: Array[Int]): Int =
    math.abs(a(0) - b(0)) + math.abs(a(1) - b(1))
}
