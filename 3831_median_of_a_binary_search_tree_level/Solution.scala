// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median_of_a_binary_search_tree_level/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private var nums: scala.collection.mutable.ArrayBuffer[Int] = _

  def levelMedian(root: TreeNode, level: Int): Int = {
    nums = scala.collection.mutable.ArrayBuffer.empty[Int]
    dfs(root, 0, level)
    if (nums.isEmpty) return -1
    nums(nums.length / 2)
  }

  private def dfs(node: TreeNode, i: Int, level: Int): Unit = {
    if (node == null) return
    dfs(node.left, i + 1, level)
    if (i == level) nums += node.value
    dfs(node.right, i + 1, level)
  }
}
