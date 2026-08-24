// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def tree2str(root: TreeNode): String = {
    if (root == null) return ""
    var result = root.value.toString
    if (root.left != null || root.right != null) result += "(" + tree2str(root.left) + ")"
    if (root.right != null) result += "(" + tree2str(root.right) + ")"
    result
  }
}
