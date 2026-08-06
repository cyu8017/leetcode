// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private val sums = scala.collection.mutable.ArrayBuffer[Long]()

  def maxProduct(root: TreeNode): Int = {
    sums.clear()
    val whole = total(root)
    var best = 0L
    for (value <- sums) best = math.max(best, value * (whole - value))
    (best % 1000000007L).toInt
  }

  private def total(node: TreeNode): Long = {
    if (node == null) return 0L
    val value = node.value + total(node.left) + total(node.right)
    sums += value
    value
  }
}
