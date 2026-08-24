// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

import scala.collection.mutable

object Solution {
  def minimumTotalPrice(n: Int, edges: Array[Array[Int]], price: Array[Int], trips: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      i += 1
    }
    val cnt = new Array[Int](n)

    def path(u: Int, p: Int, target: Int): Boolean = {
      if (u == target) {
        cnt(u) += 1
        return true
      }
      g(u).foreach { v =>
        if (v != p && path(v, u, target)) {
          cnt(u) += 1
          return true
        }
      }
      false
    }

    def dfs(u: Int, p: Int): Array[Int] = {
      var full = price(u) * cnt(u)
      var half = full / 2
      g(u).foreach { v =>
        if (v != p) {
          val child = dfs(v, u)
          full += math.min(child(0), child(1))
          half += child(0)
        }
      }
      Array(full, half)
    }

    i = 0
    while (i < trips.length) {
      path(trips(i)(0), -1, trips(i)(1))
      i += 1
    }
    val res = dfs(0, -1)
    math.min(res(0), res(1))
  }
}
