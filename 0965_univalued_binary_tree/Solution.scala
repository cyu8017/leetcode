// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isUnivalTree(root: TreeNode): Boolean = {
    if (root == null) return true
    def dfs(node: TreeNode, v: Int): Boolean = {
      if (node == null) return true
      if (node.value != v) return false
      dfs(node.left, v) && dfs(node.right, v)
    }
    dfs(root, root.value)
  }
}
