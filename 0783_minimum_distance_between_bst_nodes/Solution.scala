// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def minDiffInBST(root: TreeNode): Int = {
    var hasPrev = false
    var prev = 0
    var best = Int.MaxValue
    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      if (hasPrev) best = math.min(best, node.value - prev)
      prev = node.value
      hasPrev = true
      inorder(node.right)
    }
    inorder(root)
    best
  }
}
