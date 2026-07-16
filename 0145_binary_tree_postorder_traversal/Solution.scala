// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

import scala.collection.mutable.ListBuffer
class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)
object Solution {
  def postorderTraversal(root: TreeNode): List[Int] = {
    val result = ListBuffer[Int]()
    def traverse(node: TreeNode): Unit = if (node != null) {
      traverse(node.left)
      traverse(node.right)
      result += node.value
    }
    traverse(root)
    result.toList
  }
}