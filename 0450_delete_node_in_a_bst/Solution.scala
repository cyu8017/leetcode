// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def deleteNode(root: TreeNode, key: Int): TreeNode = {
    if (root == null) {
      return null
    }
    if (key < root.value) {
      root.left = deleteNode(root.left, key)
    } else if (key > root.value) {
      root.right = deleteNode(root.right, key)
    } else {
      if (root.left == null) {
        return root.right
      }
      if (root.right == null) {
        return root.left
      }
      var successor = root.right
      while (successor.left != null) {
        successor = successor.left
      }
      root.value = successor.value
      root.right = deleteNode(root.right, successor.value)
    }
    root
  }
}
