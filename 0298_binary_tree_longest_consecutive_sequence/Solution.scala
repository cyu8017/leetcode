// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def longestConsecutive(root: TreeNode): Int = dfs(root, null, 0)

  private def dfs(node: TreeNode, parent: TreeNode, length: Int): Int = {
    if (node == null) {
      return 0
    }
    val current =
      if (parent != null && parent.value + 1 == node.value) length + 1 else 1
    math.max(current, math.max(dfs(node.left, node, current), dfs(node.right, node, current)))
  }
}
