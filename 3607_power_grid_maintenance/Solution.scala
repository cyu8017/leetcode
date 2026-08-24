// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

object Solution {
  def processQueries(c: Int, connections: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val parent = Array.tabulate(c + 1)(i => i)

    def find(x0: Int): Int = {
      var x = x0
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) {
        if (ra < rb) parent(rb) = ra
        else parent(ra) = rb
      }
    }

    for (e <- connections) unite(e(0), e(1))
    val online = Array.fill(c + 1)(true)
    val comp = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    var i = 1
    while (i <= c) {
      val r = find(i)
      if (!comp.contains(r)) comp(r) = new java.util.ArrayList[Integer]()
      comp(r).add(i)
      i += 1
    }
    for (ids <- comp.values) java.util.Collections.sort(ids)
    val ptr = scala.collection.mutable.HashMap.empty[Int, Int]
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      val t = q(0)
      val x = q(1)
      if (t == 2) online(x) = false
      else if (online(x)) ans.add(x)
      else {
        val r = find(x)
        val ids = comp(r)
        var p = ptr.getOrElse(r, 0)
        while (p < ids.size() && !online(ids.get(p))) p += 1
        ptr(r) = p
        ans.add(if (p < ids.size()) ids.get(p) else -1)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
