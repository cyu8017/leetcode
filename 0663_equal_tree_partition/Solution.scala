// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def checkEqualTree(root: TreeNode): Boolean = {
    val subtreeSums = mutable.ArrayBuffer.empty[Int]
    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val total = node.value + dfs(node.left) + dfs(node.right)
      subtreeSums += total
      total
    }
    val total = dfs(root)
    if (subtreeSums.nonEmpty) subtreeSums.remove(subtreeSums.size - 1)
    if (total % 2 != 0) return false
    val half = total / 2
    subtreeSums.exists(_ == half)
  }
}
