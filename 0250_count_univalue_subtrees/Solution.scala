// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def countUnivalSubtrees(root: TreeNode): Int = {
    var count = 0

    def dfs(node: TreeNode): Boolean = {
      if (node == null) {
        true
      } else {
        val leftOk = dfs(node.left)
        val rightOk = dfs(node.right)
        if (!leftOk || !rightOk) {
          false
        } else if (node.left != null && node.left.value != node.value) {
          false
        } else if (node.right != null && node.right.value != node.value) {
          false
        } else {
          count += 1
          true
        }
      }
    }

    dfs(root)
    count
  }
}
