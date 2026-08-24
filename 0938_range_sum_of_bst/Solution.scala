// LeetCode 0938 - Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def rangeSumBST(root: TreeNode, low: Int, high: Int): Int = {
    if (root == null) return 0
    if (root.value < low) return rangeSumBST(root.right, low, high)
    if (root.value > high) return rangeSumBST(root.left, low, high)
    root.value + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
  }
}
