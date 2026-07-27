// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    var found = 0
    def matches(node: TreeNode, target: TreeNode): Boolean =
      target != null && (node.eq(target) || node.value == target.value)
    def dfs(node: TreeNode): TreeNode = {
      if (node == null) return null
      val left = dfs(node.left)
      val right = dfs(node.right)
      var hit = false
      if (matches(node, p)) { found += 1; hit = true }
      if (matches(node, q)) { found += 1; hit = true }
      if (hit) return node
      if (left != null && right != null) node else if (left != null) left else right
    }
    val ans = dfs(root)
    if (found == 2) ans else null
  }
}
