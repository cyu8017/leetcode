// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def binaryTreePaths(root: TreeNode): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]

    def dfs(node: TreeNode, path: List[String]): Unit = {
      if (node == null) {
        return
      }
      val nextPath = path :+ node.value.toString
      if (node.left == null && node.right == null) {
        result += nextPath.mkString("->")
      } else {
        dfs(node.left, nextPath)
        dfs(node.right, nextPath)
      }
    }

    dfs(root, Nil)
    result.toList
  }
}
