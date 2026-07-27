// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def lowestCommonAncestor(root: TreeNode, nodes: Array[TreeNode]): TreeNode = {
    val targets = nodes.toSet
    def dfs(node: TreeNode): TreeNode = {
      if (node == null) return null
      val l = dfs(node.left)
      val r = dfs(node.right)
      if (targets.contains(node) || (l != null && r != null)) return node
      if (l != null) l else r
    }
    dfs(root)
  }
}
