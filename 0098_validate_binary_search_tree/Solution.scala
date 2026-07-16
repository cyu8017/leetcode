// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isValidBST(root: TreeNode): Boolean = {
    def valid(node: TreeNode, low: Long, high: Long): Boolean = {
      if (node == null) {
        return true
      }
      val v = node.value.toLong
      if (!(low < v && v < high)) {
        return false
      }
      valid(node.left, low, v) && valid(node.right, v, high)
    }

    valid(root, Long.MinValue, Long.MaxValue)
  }
}
