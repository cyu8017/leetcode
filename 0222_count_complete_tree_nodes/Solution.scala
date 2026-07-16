// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def countNodes(root: TreeNode): Int = {
    if (root == null) {
      0
    } else {
      val left = leftDepth(root)
      val right = rightDepth(root)
      if (left == right) {
        (1 << left) - 1
      } else {
        1 + countNodes(root.left) + countNodes(root.right)
      }
    }
  }

  private def leftDepth(node: TreeNode): Int = {
    var depth = 0
    var current = node
    while (current != null) {
      depth += 1
      current = current.left
    }
    depth
  }

  private def rightDepth(node: TreeNode): Int = {
    var depth = 0
    var current = node
    while (current != null) {
      depth += 1
      current = current.right
    }
    depth
  }
}
