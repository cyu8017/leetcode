// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

object Solution {
  def areConnected(n: Int, threshold: Int, queries: Array[Array[Int]]): Array[Boolean] = {
    val parent = Array.tabulate(n + 1)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (cur != parent(cur)) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    var d = threshold + 1
    while (d <= n) {
      var x = 2 * d
      while (x <= n) {
        val a = find(d)
        val b = find(x)
        if (a != b) parent(b) = a
        x += d
      }
      d += 1
    }
    queries.map(q => find(q(0)) == find(q(1)))
  }
}
