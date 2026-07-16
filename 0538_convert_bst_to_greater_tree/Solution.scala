// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def convertBST(root: TreeNode): Unit = {
    var running = 0

    def reverseInorder(node: TreeNode): Unit = {
      if (node == null) {
        return
      }
      reverseInorder(node.right)
      running += node.value
      node.value = running
      reverseInorder(node.left)
    }

    reverseInorder(root)
  }
}
