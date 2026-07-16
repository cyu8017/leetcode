// LeetCode 0236 - Lowest Common Ancestor of a Binary Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    if (root == null || root.eq(p) || root.eq(q)) {
      root
    } else {
      val left = lowestCommonAncestor(root.left, p, q)
      val right = lowestCommonAncestor(root.right, p, q)
      if (left != null && right != null) {
        root
      } else if (left != null) {
        left
      } else {
        right
      }
    }
  }
}
