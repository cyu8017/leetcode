// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def sumNumbers(root: TreeNode): Int = {
    def dfs(node: TreeNode, current: Int): Int = {
      if (node == null) 0
      else {
        val value = current * 10 + node.value
        if (node.left == null && node.right == null) value
        else dfs(node.left, value) + dfs(node.right, value)
      }
    }
    dfs(root, 0)
  }
}