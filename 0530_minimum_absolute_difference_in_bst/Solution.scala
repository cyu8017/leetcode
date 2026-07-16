// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def getMinimumDifference(root: TreeNode): Int = {
    var best = Int.MaxValue
    var previous: Option[Int] = None

    def inorder(node: TreeNode): Unit = {
      if (node == null) {
        return
      }
      inorder(node.left)
      previous.foreach(prev => best = math.min(best, node.value - prev))
      previous = Some(node.value)
      inorder(node.right)
    }

    inorder(root)
    best
  }
}
