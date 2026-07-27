// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def correctBinaryTree(root: TreeNode): TreeNode = {
    val seen = scala.collection.mutable.Set.empty[TreeNode]
    def dfs(node: TreeNode): TreeNode = {
      if (node == null) return null
      if (node.right != null && seen.contains(node.right)) return null
      seen += node
      node.right = dfs(node.right)
      node.left = dfs(node.left)
      node
    }
    dfs(root)
  }
}
