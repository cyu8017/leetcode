// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findDistance(root: TreeNode, p: Int, q: Int): Int = {
    val graph = mutable.Map.empty[Int, mutable.ListBuffer[Int]]

    def dfs(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) {
        return
      }
      graph.getOrElseUpdate(node.value, mutable.ListBuffer.empty[Int])
      if (parent != null) {
        graph(node.value) += parent.value
        graph(parent.value) += node.value
      }
      dfs(node.left, node)
      dfs(node.right, node)
    }

    dfs(root, null)
    val queue = mutable.Queue((p, 0))
    val seen = mutable.Set(p)
    while (queue.nonEmpty) {
      val (node, dist) = queue.dequeue()
      if (node == q) {
        return dist
      }
      for (nei <- graph(node)) {
        if (seen.add(nei)) {
          queue.enqueue((nei, dist + 1))
        }
      }
    }
    -1
  }
}
