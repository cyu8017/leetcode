// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

object Solution {
  def eventualSafeNodes(graph: Array[Array[Int]]): List[Int] = {
    val n = graph.length
    val color = Array.ofDim[Int](n)
    def dfs(node: Int): Boolean = {
      if (color(node) != 0) return color(node) == 2
      color(node) = 1
      graph(node).foreach { nei => if (!dfs(nei)) return false }
      color(node) = 2
      true
    }
    (0 until n).filter(dfs).toList
  }
}
