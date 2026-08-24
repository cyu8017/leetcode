// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

object Solution {
  def isBipartite(graph: Array[Array[Int]]): Boolean = {
    val color = Array.fill(graph.length)(-1)
    def dfs(node: Int, c: Int): Boolean = {
      color(node) = c
      graph(node).foreach { nei =>
        if (color(nei) == -1) {
          if (!dfs(nei, c ^ 1)) return false
        } else if (color(nei) == c) return false
      }
      true
    }
    graph.indices.foreach { node =>
      if (color(node) == -1 && !dfs(node, 0)) return false
    }
    true
  }
}
