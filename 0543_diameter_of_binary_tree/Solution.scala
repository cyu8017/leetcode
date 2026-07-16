// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def diameterOfBinaryTree(root: TreeNode): Int = {
    var best = 0

    def depth(node: TreeNode): Int = {
      if (node == null) {
        return 0
      }
      val left = depth(node.left)
      val right = depth(node.right)
      best = math.max(best, left + right)
      1 + math.max(left, right)
    }

    depth(root)
    best
  }
}
