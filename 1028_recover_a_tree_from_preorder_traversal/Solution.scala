// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def recoverFromPreorder(traversal: String): TreeNode = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[TreeNode]
    var i = 0
    val n = traversal.length
    while (i < n) {
      var depth = 0
      while (i < n && traversal(i) == '-') {
        depth += 1
        i += 1
      }
      val start = i
      while (i < n && traversal(i).isDigit) i += 1
      val node = new TreeNode(traversal.substring(start, i).toInt)
      while (stack.length > depth) stack.remove(stack.length - 1)
      if (stack.nonEmpty) {
        if (stack.last.left == null) stack.last.left = node
        else stack.last.right = node
      }
      stack += node
    }
    stack.head
  }
}
