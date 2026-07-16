// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node(_value: Int = 0, _left: Node = null, _right: Node = null, _parent: Node = null) {
  var value: Int = _value
  var left: Node = _left
  var right: Node = _right
  var parent: Node = _parent
}

object Solution {
  def inorderSuccessor(node: Node): Node = {
    if (node.right != null) {
      var current = node.right
      while (current.left != null) current = current.left
      return current
    }
    var current: Node = node
    while (current.parent != null && current eq current.parent.right) {
      current = current.parent
    }
    current.parent
  }
}
