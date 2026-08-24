// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

object Solution {
  def minIncrease(n: Int, edges: Array[Array[Int]], cost: Array[Int]): Int = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    var ans = 0

    def dfs(u: Int, p: Int): Long = {
      if (graph(u).size() == 1 && p != -1) return cost(u)
      val childVals = new java.util.ArrayList[java.lang.Long]()
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) childVals.add(dfs(v, u))
      }
      if (childVals.isEmpty) return cost(u)
      var mx = 0L
      val cit = childVals.iterator()
      while (cit.hasNext) mx = math.max(mx, cit.next())
      val cit2 = childVals.iterator()
      while (cit2.hasNext) if (cit2.next() < mx) ans += 1
      mx + cost(u)
    }

    dfs(0, -1)
    ans
  }
}
