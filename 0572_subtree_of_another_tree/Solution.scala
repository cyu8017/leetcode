// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isSubtree(root: TreeNode, subRoot: TreeNode): Boolean = {
    if (root == null) return false
    same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
  }

  private def same(a: TreeNode, b: TreeNode): Boolean = {
    if (a == null || b == null) return a == b
    a.value == b.value && same(a.left, b.left) && same(a.right, b.right)
  }
}
