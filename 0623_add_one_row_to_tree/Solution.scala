// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def addOneRow(root: TreeNode, `val`: Int, depth: Int): TreeNode = {
    if (depth == 1) return new TreeNode(`val`, root, null)
    dfs(root, 1, `val`, depth)
    root
  }

  private def dfs(node: TreeNode, current: Int, value: Int, depth: Int): Unit = {
    if (node == null) return
    if (current == depth - 1) {
      node.left = new TreeNode(value, node.left, null)
      node.right = new TreeNode(value, null, node.right)
      return
    }
    dfs(node.left, current + 1, value, depth)
    dfs(node.right, current + 1, value, depth)
  }
}
