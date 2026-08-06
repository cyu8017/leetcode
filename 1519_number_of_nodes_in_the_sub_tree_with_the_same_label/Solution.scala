// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

object Solution {
  def countSubTrees(n: Int, edges: Array[Array[Int]], labels: String): Array[Int] = {
    val graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (Array(a, b) <- edges) {
      graph(a) += b
      graph(b) += a
    }
    val answer = Array.fill(n)(0)
    def dfs(node: Int, parent: Int): Array[Int] = {
      val counts = Array.fill(26)(0)
      val index = labels(node) - 'a'
      counts(index) = 1
      for (nei <- graph(node) if nei != parent) {
        val child = dfs(nei, node)
        for (i <- 0 until 26) counts(i) += child(i)
      }
      answer(node) = counts(index)
      counts
    }
    dfs(0, -1)
    answer
  }
}
