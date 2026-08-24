// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def insertIntoBST(root: TreeNode, `val`: Int): TreeNode = {
    if (root == null) return new TreeNode(`val`)
    var node = root
    var done = false
    while (!done) {
      if (`val` < node.value) {
        if (node.left == null) {
          node.left = new TreeNode(`val`)
          done = true
        } else node = node.left
      } else {
        if (node.right == null) {
          node.right = new TreeNode(`val`)
          done = true
        } else node = node.right
      }
    }
    root
  }
}
