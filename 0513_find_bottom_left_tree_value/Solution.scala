// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findBottomLeftValue(root: TreeNode): Int = {
    val queue = mutable.Queue[TreeNode](root)
    var leftmost = root.value
    while (queue.nonEmpty) {
      val levelSize = queue.size
      for (index <- 0 until levelSize) {
        val node = queue.dequeue()
        if (index == 0) {
          leftmost = node.value
        }
        if (node.left != null) {
          queue.enqueue(node.left)
        }
        if (node.right != null) {
          queue.enqueue(node.right)
        }
      }
    }
    leftmost
  }
}
