// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def closestKValues(root: TreeNode, target: Double, k: Int): List[Int] = {
    val values = scala.collection.mutable.ListBuffer.empty[Int]
    inorder(root, values)

    var lo = 0
    var hi = values.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (values(mid) < target) lo = mid + 1
      else hi = mid
    }

    var left = lo - 1
    var right = lo
    val result = scala.collection.mutable.ListBuffer.empty[Int]
    while (result.length < k) {
      if (right >= values.length ||
          (left >= 0 && math.abs(values(left) - target) <= math.abs(values(right) - target))) {
        result += values(left)
        left -= 1
      } else {
        result += values(right)
        right += 1
      }
    }
    result.toList
  }

  private def inorder(node: TreeNode, values: scala.collection.mutable.ListBuffer[Int]): Unit = {
    if (node == null) return
    inorder(node.left, values)
    values += node.value
    inorder(node.right, values)
  }
}
