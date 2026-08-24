// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def averageOfLevels(root: TreeNode): Array[Double] = {
    if (root == null) return Array.empty[Double]
    val result = mutable.ArrayBuffer.empty[Double]
    val queue = mutable.Queue[TreeNode](root)
    while (queue.nonEmpty) {
      val count = queue.size
      var total = 0L
      var i = 0
      while (i < count) {
        val node = queue.dequeue()
        total += node.value
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
        i += 1
      }
      result += total.toDouble / count
    }
    result.toArray
  }
}
