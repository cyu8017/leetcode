// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def pathSum(root: TreeNode, targetSum: Int): Int = {
    val prefixCounts = mutable.Map(0 -> 1)
    dfs(root, 0, targetSum, prefixCounts)
  }

  private def dfs(
      node: TreeNode,
      current: Int,
      targetSum: Int,
      prefixCounts: mutable.Map[Int, Int]
  ): Int = {
    if (node == null) {
      return 0
    }

    val updated = current + node.value
    var total = prefixCounts.getOrElse(updated - targetSum, 0)
    prefixCounts(updated) = prefixCounts.getOrElse(updated, 0) + 1
    total += dfs(node.left, updated, targetSum, prefixCounts)
    total += dfs(node.right, updated, targetSum, prefixCounts)
    prefixCounts(updated) -= 1
    total
  }
}
