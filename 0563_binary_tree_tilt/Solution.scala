// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findTilt(root: TreeNode): Int = {
    var total = 0
    def subtreeSum(node: TreeNode): Int = {
      if (node == null) return 0
      val left = subtreeSum(node.left)
      val right = subtreeSum(node.right)
      total += math.abs(left - right)
      node.value + left + right
    }
    subtreeSum(root)
    total
  }
}
