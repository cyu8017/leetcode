// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isBalanced(root: TreeNode): Boolean = {
    height(root) != -1
  }

  private def height(node: TreeNode): Int = {
    if (node == null) {
      return 0
    }
    val left = height(node.left)
    if (left == -1) {
      return -1
    }
    val right = height(node.right)
    if (right == -1) {
      return -1
    }
    if (math.abs(left - right) > 1) {
      return -1
    }
    1 + math.max(left, right)
  }
}
