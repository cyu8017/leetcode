// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def longestUnivaluePath(root: TreeNode): Int = {
    var best = 0
    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val left = dfs(node.left)
      val right = dfs(node.right)
      val leftPath = if (node.left != null && node.left.value == node.value) left + 1 else 0
      val rightPath = if (node.right != null && node.right.value == node.value) right + 1 else 0
      best = math.max(best, leftPath + rightPath)
      math.max(leftPath, rightPath)
    }
    dfs(root)
    best
  }
}
