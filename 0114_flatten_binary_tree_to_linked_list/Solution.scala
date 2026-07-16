// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def flatten(root: TreeNode): Unit = {
    def flattenTail(node: TreeNode): TreeNode = {
      if (node == null) null
      else {
        val leftTail = flattenTail(node.left)
        val rightTail = flattenTail(node.right)
        if (leftTail != null) {
          leftTail.right = node.right
          node.right = node.left
          node.left = null
        }
        if (rightTail != null) rightTail else if (leftTail != null) leftTail else node
      }
    }
    flattenTail(root)
  }
}