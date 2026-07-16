// LeetCode 0102 - Binary Tree Level Order Traversal
// https://leetcode.com/problems/binary-tree-level-order-traversal/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def levelOrder(root: TreeNode): List[List[Int]] = {
    if (root == null) {
      return List.empty
    }

    val result = mutable.ListBuffer[List[Int]]()
    val queue = mutable.Queue[TreeNode](root)

    while (queue.nonEmpty) {
      val size = queue.size
      val level = mutable.ListBuffer[Int]()
      for (_ <- 0 until size) {
        val node = queue.dequeue()
        level += node.value
        if (node.left != null) {
          queue.enqueue(node.left)
        }
        if (node.right != null) {
          queue.enqueue(node.right)
        }
      }
      result += level.toList
    }

    result.toList
  }
}
