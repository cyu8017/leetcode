// LeetCode 0112 - Path Sum
// https://leetcode.com/problems/path-sum/

object Solution {
  def hasPathSum(root: TreeNode, targetSum: Int): Boolean = {
    if (root == null) false
    else if (root.left == null && root.right == null) root.value == targetSum
    else hasPathSum(root.left, targetSum - root.value) ||
      hasPathSum(root.right, targetSum - root.value)
  }
}

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}