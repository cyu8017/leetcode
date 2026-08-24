// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

object Solution {
  def countGoodNodes(edges: Array[Array[Int]]): Int = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0
    def dfs(a: Int, fa: Int): Int = {
      var pre = -1
      var cnt = 1
      var ok = 1
      for (b <- g(a) if b != fa) {
        val cur = dfs(b, a)
        cnt += cur
        if (pre < 0) pre = cur
        else if (pre != cur) ok = 0
      }
      ans += ok
      cnt
    }
    dfs(0, -1)
    ans
  }
}
