// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def twoSumBSTs(root1: TreeNode, root2: TreeNode, target: Int): Boolean = {
    val values = scala.collection.mutable.Set.empty[Int]
    val stack = scala.collection.mutable.Stack[TreeNode]()
    if (root1 != null) stack.push(root1)
    while (stack.nonEmpty) {
      val node = stack.pop()
      values += node.value
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    if (root2 != null) stack.push(root2)
    while (stack.nonEmpty) {
      val node = stack.pop()
      if (values.contains(target - node.value)) return true
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    false
  }
}
