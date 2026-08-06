// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def lcaDeepestLeaves(root: TreeNode): TreeNode = {
    def dfs(node: TreeNode): (TreeNode, Int) = {
      if (node == null) return (null, 0)
      val (lNode, lDepth) = dfs(node.left)
      val (rNode, rDepth) = dfs(node.right)
      if (lDepth > rDepth) (lNode, lDepth + 1)
      else if (rDepth > lDepth) (rNode, rDepth + 1)
      else (node, lDepth + 1)
    }
    dfs(root)._1
  }
}
