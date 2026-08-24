// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isCousins(root: TreeNode, x: Int, y: Int): Boolean = {
    val depth = scala.collection.mutable.Map.empty[Int, Int]
    val parent = scala.collection.mutable.Map.empty[Int, TreeNode]
    def dfs(node: TreeNode, p: TreeNode, d: Int): Unit = {
      if (node == null) return
      depth(node.value) = d
      parent(node.value) = p
      dfs(node.left, node, d + 1)
      dfs(node.right, node, d + 1)
    }
    dfs(root, null, 0)
    depth(x) == depth(y) && parent(x) != parent(y)
  }
}
