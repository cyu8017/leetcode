// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

object Solution {
  def kthSmallest(par: Array[Int], vals: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = par.length
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < n) { g(par(i)).add(i); i += 1 }
    val xorPath = new Array[Int](n)

    def dfs(u: Int): Unit = {
      xorPath(u) ^= vals(u)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        xorPath(v) = xorPath(u)
        dfs(v)
      }
    }

    val inT = new Array[Int](n)
    val outT = new Array[Int](n)
    val order = new java.util.ArrayList[Integer]()

    def dfs2(u: Int): Unit = {
      inT(u) = order.size()
      order.add(xorPath(u))
      val it = g(u).iterator()
      while (it.hasNext) dfs2(it.next())
      outT(u) = order.size()
    }

    dfs(0)
    dfs2(0)
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val u = queries(i)(0)
      val k = queries(i)(1)
      val sub = new java.util.ArrayList[Integer](order.subList(inT(u), outT(u)))
      java.util.Collections.sort(sub)
      val uniq = new java.util.ArrayList[Integer]()
      val it = sub.iterator()
      while (it.hasNext) {
        val x = it.next()
        if (uniq.isEmpty || uniq.get(uniq.size() - 1) != x) uniq.add(x)
      }
      ans(i) = if (k > uniq.size()) -1 else uniq.get(k - 1)
      i += 1
    }
    ans
  }
}
