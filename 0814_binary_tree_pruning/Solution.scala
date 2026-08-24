// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def pruneTree(root: TreeNode): TreeNode = {
    if (root == null) return null
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if (root.value == 0 && root.left == null && root.right == null) null else root
  }
}
