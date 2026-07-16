// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def kthSmallest(root: TreeNode, k: Int): Int = {
    val stack = mutable.ArrayDeque.empty[TreeNode]
    var current: TreeNode = root
    var remaining = k

    while (current != null || stack.nonEmpty) {
      while (current != null) {
        stack.append(current)
        current = current.left
      }
      current = stack.removeLast()
      remaining -= 1
      if (remaining == 0) {
        return current.value
      }
      current = current.right
    }

    -1
  }
}
