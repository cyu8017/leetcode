// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

object Solution {
  def validTree(n: Int, edges: Array[Array[Int]]): Boolean = {
    if (edges.length != n - 1) {
      return false
    }
    val parent = Array.tabulate(n)(identity)

    def find(node: Int): Int = {
      if (parent(node) != node) {
        parent(node) = find(parent(node))
      }
      parent(node)
    }

    edges.foreach { edge =>
      val rootLeft = find(edge(0))
      val rootRight = find(edge(1))
      if (rootLeft == rootRight) {
        return false
      }
      parent(rootLeft) = rootRight
    }
    true
  }
}
