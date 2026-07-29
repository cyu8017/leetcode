// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def bstToGst(root: TreeNode): TreeNode = {
    var total = 0
    def reverseInorder(node: TreeNode): Unit = {
      if (node == null) return
      reverseInorder(node.right)
      total += node.value
      node.value = total
      reverseInorder(node.left)
    }
    reverseInorder(root)
    root
  }
}
