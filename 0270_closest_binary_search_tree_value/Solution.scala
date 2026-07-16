// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def closestValue(root: TreeNode, target: Double): Int = {
    var closest = root.value
    var current: TreeNode = root
    while (current != null) {
      if (math.abs(closest - target) > math.abs(current.value - target)) {
        closest = current.value
      }
      if (current.value.toDouble == target) {
        return current.value
      }
      current = if (target < current.value) current.left else current.right
    }
    closest
  }
}
