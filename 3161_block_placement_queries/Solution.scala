// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

object Solution {
  private class FenwickMax(n: Int) {
    val vals: Array[Int] = new Array[Int](n + 1)

    def maximize(i0: Int, `val`: Int): Unit = {
      var i = i0
      while (i < vals.length) {
        vals(i) = math.max(vals(i), `val`)
        i += i & -i
      }
    }

    def get(i0: Int): Int = {
      var i = i0
      var res = 0
      while (i > 0) {
        res = math.max(res, vals(i))
        i -= i & -i
      }
      res
    }
  }

  private def lowerBound(a: java.util.ArrayList[Integer], x: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def getResults(queries: Array[Array[Int]]): Array[Boolean] = {
    var n = queries.length * 3
    if (n > 50000) n = 50000
    val tree = new FenwickMax(n + 1)
    val obs = new java.util.ArrayList[Integer]()
    obs.add(0)
    obs.add(n)
    queries.foreach { q =>
      if (q(0) == 1) {
        val x = q(1)
        val idx = lowerBound(obs, x)
        if (idx == obs.size() || obs.get(idx) != x) obs.add(idx, x)
      }
    }
    var i = 0
    while (i + 1 < obs.size()) {
      tree.maximize(obs.get(i + 1), obs.get(i + 1) - obs.get(i))
      i += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Boolean]
    i = queries.length - 1
    while (i >= 0) {
      val typ = queries(i)(0)
      val x = queries(i)(1)
      if (typ == 1) {
        val j = lowerBound(obs, x)
        val prev = obs.get(j - 1)
        val next = obs.get(j + 1)
        obs.remove(j)
        tree.maximize(next, next - prev)
      } else {
        val sz = queries(i)(2)
        val j = lowerBound(obs, x + 1) - 1
        val prev = obs.get(j)
        ans += (tree.get(prev) >= sz || x - prev >= sz)
      }
      i -= 1
    }
    ans.reverse.toArray
  }
}
