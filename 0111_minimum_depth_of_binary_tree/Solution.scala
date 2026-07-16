// LeetCode 0111 - Minimum Depth of Binary Tree
class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def minDepth(root: TreeNode): Int = {
    if (root == null) 0
    else if (root.left == null) 1 + minDepth(root.right)
    else if (root.right == null) 1 + minDepth(root.left)
    else 1 + Math.min(minDepth(root.left), minDepth(root.right))
  }
}