// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def splitBST(root: TreeNode, target: Int): Array[TreeNode] = {
    if (root == null) return Array(null, null)
    if (root.value <= target) {
      val parts = splitBST(root.right, target)
      root.right = parts(0)
      Array(root, parts(1))
    } else {
      val leftParts = splitBST(root.left, target)
      root.left = leftParts(1)
      Array(leftParts(0), root)
    }
  }
}
