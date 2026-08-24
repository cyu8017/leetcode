// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def heightOfTree(root: TreeNode): Int = {
    if (root == null) return -1
    dfs(root)
  }

  private def dfs(node: TreeNode): Int = {
    if (node == null) return -1
    if (node.left != null && node.left.right == node) return dfs(node.right) + 1
    if (node.right != null && node.right.left == node) return dfs(node.left) + 1
    math.max(dfs(node.left), dfs(node.right)) + 1
  }
}
