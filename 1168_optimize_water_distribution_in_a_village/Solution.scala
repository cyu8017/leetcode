// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

object Solution {
  def minCostToSupplyWater(n: Int, wells: Array[Int], pipes: Array[Array[Int]]): Int = {
    val parent = Array.tabulate(n + 1)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    val edges = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (i <- wells.indices) edges += Array(0, i + 1, wells(i))
    edges ++= pipes
    val sorted = edges.sortBy(_(2))
    var ans = 0
    for (e <- sorted) {
      val a = find(e(0))
      val b = find(e(1))
      if (a != b) {
        parent(b) = a
        ans += e(2)
      }
    }
    ans
  }
}
