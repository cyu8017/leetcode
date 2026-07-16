// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode(var x: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode): TreeNode = {
    var current = root
    while (current != null) {
      if (p.x < current.x && q.x < current.x) {
        current = current.left
      } else if (p.x > current.x && q.x > current.x) {
        current = current.right
      } else {
        return current
      }
    }
    current
  }
}
