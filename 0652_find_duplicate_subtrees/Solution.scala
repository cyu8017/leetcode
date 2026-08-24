// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findDuplicateSubtrees(root: TreeNode): List[TreeNode] = {
    val counts = mutable.Map.empty[String, Int]
    val result = mutable.ArrayBuffer.empty[TreeNode]
    def serialize(node: TreeNode): String = {
      if (node == null) return "#"
      val key = node.value + "," + serialize(node.left) + "," + serialize(node.right)
      val count = counts.getOrElse(key, 0) + 1
      counts(key) = count
      if (count == 2) result += node
      key
    }
    serialize(root)
    result.toList
  }
}
