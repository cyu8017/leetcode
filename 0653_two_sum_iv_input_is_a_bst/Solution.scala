// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findTarget(root: TreeNode, k: Int): Boolean = {
    val seen = mutable.Set.empty[Int]
    def dfs(node: TreeNode): Boolean = {
      if (node == null) return false
      if (seen.contains(k - node.value)) return true
      seen += node.value
      dfs(node.left) || dfs(node.right)
    }
    dfs(root)
  }
}
