// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

import scala.collection.mutable.ListBuffer
class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)
object Solution {
  def preorderTraversal(root: TreeNode): List[Int] = {
    val result = ListBuffer[Int]()
    def traverse(node: TreeNode): Unit = if (node != null) {
      result += node.value
      traverse(node.left)
      traverse(node.right)
    }
    traverse(root)
    result.toList
  }
}