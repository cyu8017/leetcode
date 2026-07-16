// LeetCode 0226 - Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def invertTree(root: TreeNode): TreeNode = {
    if (root == null) {
      null
    } else {
      val left = invertTree(root.left)
      val right = invertTree(root.right)
      root.left = right
      root.right = left
      root
    }
  }
}
