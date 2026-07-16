// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def inorderTraversal(root: TreeNode): List[Int] = {
    val result = scala.collection.mutable.ListBuffer[Int]()
    val stack = scala.collection.mutable.Stack[TreeNode]()
    var current = root
    while (current != null || stack.nonEmpty) {
      while (current != null) {
        stack.push(current)
        current = current.left
      }
      current = stack.pop()
      result += current.value
      current = current.right
    }
    result.toList
  }
}
