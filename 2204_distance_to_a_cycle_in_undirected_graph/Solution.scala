// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

object Solution {
  def distanceToCycle(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val deg = Array.fill(n)(0)
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      deg(e(0)) += 1
      deg(e(1)) += 1
    }
    val q = scala.collection.mutable.Queue.empty[Int]
    var i = 0
    while (i < n) {
      if (deg(i) == 1) q.enqueue(i)
      i += 1
    }
    val onCycle = Array.fill(n)(true)
    while (q.nonEmpty) {
      val u = q.dequeue()
      onCycle(u) = false
      for (v <- g(u)) {
        deg(v) -= 1
        if (deg(v) == 1) q.enqueue(v)
      }
    }
    val ans = Array.fill(n)(-1)
    val qq = scala.collection.mutable.Queue.empty[Int]
    i = 0
    while (i < n) {
      if (onCycle(i)) {
        ans(i) = 0
        qq.enqueue(i)
      }
      i += 1
    }
    while (qq.nonEmpty) {
      val u = qq.dequeue()
      for (v <- g(u) if ans(v) == -1) {
        ans(v) = ans(u) + 1
        qq.enqueue(v)
      }
    }
    ans
  }
}
