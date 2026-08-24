// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

object Solution {
  def treeQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n + 1)(new java.util.ArrayList[Array[Int]]())
    val weight = scala.collection.mutable.HashMap.empty[Long, Int]
    for (e <- edges) {
      val u = e(0); val v = e(1); val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w))
      val a = math.min(u, v)
      val b = math.max(u, v)
      weight((a.toLong << 32) | b) = w
    }
    val inT = new Array[Int](n + 1)
    val outT = new Array[Int](n + 1)
    val dist = new Array[Int](n + 1)
    val parent = new Array[Int](n + 1)
    var time = 0

    def dfs(u: Int, p: Int): Unit = {
      inT(u) = time
      time += 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val e = it.next()
        val to = e(0); val w = e(1)
        if (to != p) {
          parent(to) = u
          dist(to) = dist(u) + w
          dfs(to, u)
        }
      }
      outT(u) = time - 1
    }

    dfs(1, 0)
    val bit = new Array[Int](n + 2)

    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i <= n) {
        bit(i) += v
        i += i & -i
      }
    }

    def rangeAdd(l: Int, r: Int, v: Int): Unit = {
      add(l + 1, v)
      add(r + 2, -v)
    }

    def point(i0: Int): Int = {
      var s = 0
      var i = i0 + 1
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }

    var i = 1
    while (i <= n) {
      rangeAdd(inT(i), inT(i), dist(i))
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      if (q(0) == 1) {
        val u = q(1); val v = q(2); val nw = q(3)
        val a = math.min(u, v)
        val b = math.max(u, v)
        val key = (a.toLong << 32) | b
        val ow = weight(key)
        val delta = nw - ow
        weight(key) = nw
        val child = if (parent(u) == v) u else v
        rangeAdd(inT(child), outT(child), delta)
      } else {
        ans.add(point(inT(q(1))))
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
