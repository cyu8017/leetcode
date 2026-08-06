// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

object Solution {
  def minimumCost(n: Int, connections: Array[Array[Int]]): Int = {
    val parent = Array.tabulate(n + 1)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    val edges = connections.sortBy(_(2))
    var cost = 0
    var used = 0
    for (e <- edges) {
      val a = find(e(0))
      val b = find(e(1))
      if (a != b) {
        parent(b) = a
        cost += e(2)
        used += 1
        if (used == n - 1) return cost
      }
    }
    -1
  }
}
