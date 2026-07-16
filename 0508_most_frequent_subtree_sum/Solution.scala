// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findFrequentTreeSum(root: TreeNode): Array[Int] = {
    val counts = mutable.Map.empty[Int, Int]
    subtreeSum(root, counts)
    if (counts.isEmpty) return Array.empty[Int]
    val best = counts.values.max
    counts.filter(_._2 == best).keys.toArray.sorted
  }

  private def subtreeSum(node: TreeNode, counts: mutable.Map[Int, Int]): Int = {
    if (node == null) return 0
    val total = node.value + subtreeSum(node.left, counts) + subtreeSum(node.right, counts)
    counts(total) = counts.getOrElse(total, 0) + 1
    total
  }
}
