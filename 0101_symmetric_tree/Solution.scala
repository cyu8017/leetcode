// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isSymmetric(root: TreeNode): Boolean = {
    if (root == null) {
      true
    } else {
      mirrors(root.left, root.right)
    }
  }

  private def mirrors(left: TreeNode, right: TreeNode): Boolean = {
    if (left == null && right == null) {
      true
    } else if (left == null || right == null || left.value != right.value) {
      false
    } else {
      mirrors(left.left, right.right) && mirrors(left.right, right.left)
    }
  }
}
