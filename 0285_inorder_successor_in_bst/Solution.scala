// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def inorderSuccessor(root: TreeNode, p: TreeNode): TreeNode = {
    if (p.right != null) {
      var current = p.right
      while (current.left != null) {
        current = current.left
      }
      return current
    }

    var successor: TreeNode = null
    var current: TreeNode = root
    while (current != null) {
      if (p.value < current.value) {
        successor = current
        current = current.left
      } else {
        current = current.right
      }
    }
    successor
  }
}
