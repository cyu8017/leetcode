// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def treeToDoublyList(root: TreeNode): TreeNode = {
    if (root == null) {
      return null
    }

    var first: TreeNode = null
    var last: TreeNode = null

    def inorder(node: TreeNode): Unit = {
      if (node == null) {
        return
      }
      inorder(node.left)
      if (last != null) {
        last.right = node
        node.left = last
      } else {
        first = node
      }
      last = node
      inorder(node.right)
    }

    inorder(root)
    if (first != null && last != null) {
      first.left = last
      last.right = first
    }
    first
  }
}
