// LeetCode 1325 - Delete Leaves With a Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def removeLeafNodes(root: TreeNode, target: Int): TreeNode = {
    if (root == null) return null
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if (root.left == null && root.right == null && root.value == target) null
    else root
  }
}
