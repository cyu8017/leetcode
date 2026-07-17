// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

object Solution {
  def getCoprimes(nums: Array[Int], edges: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val adj = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    for (e <- edges) {
      adj(e(0)) += e(1)
      adj(e(1)) += e(0)
    }

    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

    val ans = Array.fill(n)(-1)
    val path = Array.fill(51)(scala.collection.mutable.Stack.empty[(Int, Int)])

    def dfs(node: Int, parent: Int, depth: Int): Unit = {
      var bestDepth = -1
      var bestNode = -1
      val value = nums(node)
      for (d <- 1 to 50) {
        if (gcd(value, d) == 1 && path(d).nonEmpty) {
          val (candDepth, candNode) = path(d).top
          if (candDepth > bestDepth) {
            bestDepth = candDepth
            bestNode = candNode
          }
        }
      }
      ans(node) = bestNode
      path(value).push((depth, node))
      for (nxt <- adj(node)) {
        if (nxt != parent) {
          dfs(nxt, node, depth + 1)
        }
      }
      path(value).pop()
    }

    dfs(0, -1, 0)
    ans
  }
}
