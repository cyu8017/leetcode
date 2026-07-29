// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

object Solution {
  def leadsToDestination(n: Int, edges: Array[Array[Int]], source: Int, destination: Int): Boolean = {
    val graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) graph(e(0)) += e(1)
    val state = Array.fill(n)(0) // 0 unvisited, 1 in progress, 2 confirmed

    def dfs(node: Int): Boolean = {
      if (graph(node).isEmpty) return node == destination
      if (state(node) == 1) return false
      if (state(node) == 2) return true
      state(node) = 1
      for (nxt <- graph(node) if !dfs(nxt)) return false
      state(node) = 2
      true
    }

    dfs(source)
  }
}
