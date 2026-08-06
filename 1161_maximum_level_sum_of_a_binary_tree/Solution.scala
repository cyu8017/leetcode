// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maxLevelSum(root: TreeNode): Int = {
    val q = scala.collection.mutable.Queue(root)
    var bestSum = Int.MinValue
    var bestLevel = 1
    var level = 1
    while (q.nonEmpty) {
      var total = 0
      val size = q.size
      for (_ <- 0 until size) {
        val node = q.dequeue()
        total += node.value
        if (node.left != null) q.enqueue(node.left)
        if (node.right != null) q.enqueue(node.right)
      }
      if (total > bestSum) {
        bestSum = total
        bestLevel = level
      }
      level += 1
    }
    bestLevel
  }
}
