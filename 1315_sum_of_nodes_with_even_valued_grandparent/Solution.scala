// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def sumEvenGrandparent(root: TreeNode): Int = {
    def dfs(node: TreeNode, parent: TreeNode, grandparent: TreeNode): Int = {
      if (node == null) return 0
      val add = if (grandparent != null && grandparent.value % 2 == 0) node.value else 0
      add + dfs(node.left, node, parent) + dfs(node.right, node, parent)
    }
    dfs(root, null, null)
  }
}
