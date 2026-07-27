// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isEvenOddTree(root: TreeNode): Boolean = {
    if (root == null) return true
    var q = List(root)
    var level = 0
    while (q.nonEmpty) {
      var prev = if (level % 2 == 0) Int.MinValue else Int.MaxValue
      val nxt = scala.collection.mutable.ListBuffer.empty[TreeNode]
      for (node <- q) {
        if (node.value % 2 == level % 2) return false
        if (level % 2 == 0 && node.value <= prev) return false
        if (level % 2 == 1 && node.value >= prev) return false
        prev = node.value
        if (node.left != null) nxt += node.left
        if (node.right != null) nxt += node.right
      }
      q = nxt.toList
      level += 1
    }
    true
  }
}
