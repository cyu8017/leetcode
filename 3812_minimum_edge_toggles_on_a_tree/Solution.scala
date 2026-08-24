// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

object Solution {
  def minimumFlips(n: Int, edges: Array[Array[Int]], start: String, target: String): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    var i = 0
    while (i < n - 1) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      g(a).add(Array(b, i))
      g(b).add(Array(a, i))
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()

    def dfs(a: Int, fa: Int): Boolean = {
      var rev = start.charAt(a) != target.charAt(a)
      val it = g(a).iterator()
      while (it.hasNext) {
        val e = it.next()
        val b = e(0)
        val ei = e(1)
        if (b != fa && dfs(b, a)) {
          ans.add(ei)
          rev = !rev
        }
      }
      rev
    }

    if (dfs(0, -1)) return Array(-1)
    java.util.Collections.sort(ans)
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
