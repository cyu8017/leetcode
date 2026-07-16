// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def recoverTree(root: TreeNode): Unit = {
    var first: TreeNode = null
    var second: TreeNode = null
    var previous: TreeNode = null
    val stack = scala.collection.mutable.ListBuffer.empty[TreeNode]
    var current = root

    while (current != null || stack.nonEmpty) {
      while (current != null) {
        stack += current
        current = current.left
      }
      current = stack.remove(stack.length - 1)
      if (previous != null && previous.value > current.value) {
        if (first == null) {
          first = previous
        }
        second = current
      }
      previous = current
      current = current.right
    }

    if (first != null && second != null) {
      val temp = first.value
      first.value = second.value
      second.value = temp
    }
  }
}
