// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findMode(root: TreeNode): Array[Int] = {
    val counts = mutable.Map.empty[Int, Int]
    var best = 0
    inorder(root, counts, count => best = math.max(best, count))
    counts.filter(_._2 == best).keys.toArray
  }

  private def inorder(
      node: TreeNode,
      counts: mutable.Map[Int, Int],
      onCount: Int => Unit,
  ): Unit = {
    if (node == null) return
    inorder(node.left, counts, onCount)
    val count = counts.getOrElse(node.value, 0) + 1
    counts(node.value) = count
    onCount(count)
    inorder(node.right, counts, onCount)
  }
}
