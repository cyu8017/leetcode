// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maxAncestorDiff(root: TreeNode): Int = {
    def dfs(node: TreeNode, lo: Int, hi: Int): Int = {
      if (node == null) return hi - lo
      val nlo = math.min(lo, node.value)
      val nhi = math.max(hi, node.value)
      math.max(dfs(node.left, nlo, nhi), dfs(node.right, nlo, nhi))
    }
    dfs(root, root.value, root.value)
  }
}
