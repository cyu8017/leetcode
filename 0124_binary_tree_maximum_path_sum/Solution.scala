// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maxPathSum(root: TreeNode): Int = {
    var best = Int.MinValue
    def gain(node: TreeNode): Int = {
      if (node == null) 0
      else {
        val left = Math.max(gain(node.left), 0)
        val right = Math.max(gain(node.right), 0)
        best = Math.max(best, node.value + left + right)
        node.value + Math.max(left, right)
      }
    }
    gain(root)
    best
  }
}