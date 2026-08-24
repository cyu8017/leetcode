// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def widthOfBinaryTree(root: TreeNode): Int = {
    if (root == null) return 0
    val queue = mutable.Queue[(TreeNode, Long)]((root, 0L))
    var best = 0
    while (queue.nonEmpty) {
      val left = queue.head._2
      val size = queue.size
      var i = 0
      while (i < size) {
        val (node, idx) = queue.dequeue()
        best = math.max(best, (idx - left + 1).toInt)
        if (node.left != null) queue.enqueue((node.left, idx * 2))
        if (node.right != null) queue.enqueue((node.right, idx * 2 + 1))
        i += 1
      }
    }
    best
  }
}
