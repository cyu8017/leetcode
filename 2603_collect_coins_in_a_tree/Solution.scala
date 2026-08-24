// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

object Solution {
  def collectTheCoins(coins: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = coins.length
    val g = Array.fill(n)(scala.collection.mutable.Set.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val deg = Array.fill(n)(0)
    var i = 0
    while (i < n) {
      deg(i) = g(i).size
      i += 1
    }
    val q = scala.collection.mutable.Queue.empty[Int]
    i = 0
    while (i < n) {
      if (deg(i) == 1 && coins(i) == 0) q.enqueue(i)
      i += 1
    }
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).toList.foreach { v =>
        g(v) -= u
        deg(v) -= 1
        if (deg(v) == 1 && coins(v) == 0) q.enqueue(v)
      }
      g(u).clear()
      deg(u) = 0
    }
    var round = 0
    while (round < 2) {
      val leaves = scala.collection.mutable.ArrayBuffer.empty[Int]
      i = 0
      while (i < n) {
        if (deg(i) == 1) leaves += i
        i += 1
      }
      leaves.foreach { u =>
        g(u).toList.foreach { v =>
          g(v) -= u
          deg(v) -= 1
        }
        g(u).clear()
        deg(u) = 0
      }
      round += 1
    }
    var remain = 0
    i = 0
    while (i < n) {
      remain += g(i).size
      i += 1
    }
    remain
  }
}
