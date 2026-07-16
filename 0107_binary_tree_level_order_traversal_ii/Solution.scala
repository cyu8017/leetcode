// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def levelOrderBottom(root: TreeNode): List[List[Int]] = {
    if (root == null) {
      return List.empty
    }

    val result = scala.collection.mutable.ListBuffer[List[Int]]()
    val queue = scala.collection.mutable.Queue[TreeNode](root)

    while (queue.nonEmpty) {
      val size = queue.size
      val level = scala.collection.mutable.ListBuffer[Int]()
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

    result.reverse.toList
  }
}
