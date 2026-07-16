// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def largestValues(root: TreeNode): List[Int] = {
    if (root == null) {
      return List.empty
    }
    val result = mutable.ListBuffer[Int]()
    val queue = mutable.Queue[TreeNode](root)
    while (queue.nonEmpty) {
      var levelMax = Int.MinValue
      val levelSize = queue.size
      for (_ <- 0 until levelSize) {
        val node = queue.dequeue()
        levelMax = math.max(levelMax, node.value)
        if (node.left != null) {
          queue.enqueue(node.left)
        }
        if (node.right != null) {
          queue.enqueue(node.right)
        }
      }
      result += levelMax
    }
    result.toList
  }
}
