// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def closestNodes(root: TreeNode, queries: List[Int]): List[List[Int]] = {
    val vals = scala.collection.mutable.ArrayBuffer.empty[Int]
    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      vals += node.value
      inorder(node.right)
    }
    inorder(root)

    def lowerBound(q: Int): Int = {
      var lo = 0
      var hi = vals.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (vals(mid) < q) lo = mid + 1
        else hi = mid
      }
      lo
    }

    queries.map { q =>
      val j = lowerBound(q)
      val mx = if (j < vals.length) vals(j) else -1
      val mn =
        if (j < vals.length && vals(j) == q) q
        else if (j > 0) vals(j - 1)
        else -1
      List(mn, mx)
    }
  }
}
