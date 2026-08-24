// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def verticalTraversal(root: TreeNode): List[List[Int]] = {
    val nodes = scala.collection.mutable.ArrayBuffer.empty[(Int, Int, Int)]
    def dfs(node: TreeNode, row: Int, col: Int): Unit = {
      if (node == null) return
      nodes += ((col, row, node.value))
      dfs(node.left, row + 1, col - 1)
      dfs(node.right, row + 1, col + 1)
    }
    dfs(root, 0, 0)
    val sorted = nodes.sortBy(t => (t._1, t._2, t._3))
    val byCol = scala.collection.mutable.LinkedHashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    sorted.foreach { case (col, _, v) =>
      byCol.getOrElseUpdate(col, scala.collection.mutable.ArrayBuffer.empty[Int]) += v
    }
    byCol.values.map(_.toList).toList
  }
}
