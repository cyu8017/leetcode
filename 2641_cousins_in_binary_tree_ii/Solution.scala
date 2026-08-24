// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def replaceValueInTree(root: TreeNode): TreeNode = {
    if (root == null) return null
    root.value = 0
    val q = mutable.Queue.empty[TreeNode]
    q.enqueue(root)
    while (q.nonEmpty) {
      val sz = q.size
      var levelSum = 0
      val level = mutable.ArrayBuffer.empty[TreeNode]
      var i = 0
      while (i < sz) {
        val node = q.dequeue()
        level += node
        if (node.left != null) levelSum += node.left.value
        if (node.right != null) levelSum += node.right.value
        i += 1
      }
      level.foreach { node =>
        var cousin = levelSum
        if (node.left != null) cousin -= node.left.value
        if (node.right != null) cousin -= node.right.value
        if (node.left != null) {
          node.left.value = cousin
          q.enqueue(node.left)
        }
        if (node.right != null) {
          node.right.value = cousin
          q.enqueue(node.right)
        }
      }
    }
    root
  }
}
