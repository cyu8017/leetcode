// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def insertIntoMaxTree(root: TreeNode, `val`: Int): TreeNode = {
    if (root == null || `val` > root.value) {
      val node = new TreeNode(`val`)
      node.left = root
      node
    } else {
      root.right = insertIntoMaxTree(root.right, `val`)
      root
    }
  }
}
