// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def generateTrees(n: Int): List[TreeNode] = {
    if (n == 0) List.empty
    else build(1, n)
  }

  private def build(start: Int, end: Int): List[TreeNode] = {
    if (start > end) return List(null)
    val trees = scala.collection.mutable.ListBuffer[TreeNode]()
    for (rootVal <- start to end) {
      val leftTrees = build(start, rootVal - 1)
      val rightTrees = build(rootVal + 1, end)
      for (left <- leftTrees; right <- rightTrees) {
        trees += new TreeNode(rootVal, left, right)
      }
    }
    trees.toList
  }
}
