// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def sumRootToLeaf(root: TreeNode): Int = {
    def dfs(node: TreeNode, value: Int): Int = {
      if (node == null) return 0
      val next = value * 2 + node.value
      if (node.left == null && node.right == null) return next
      dfs(node.left, next) + dfs(node.right, next)
    }
    dfs(root, 0)
  }
}
