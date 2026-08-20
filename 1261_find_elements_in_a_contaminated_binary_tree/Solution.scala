// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class FindElements(_root: TreeNode) {
  private val values = scala.collection.mutable.Set.empty[Int]
  private def recover(node: TreeNode, value: Int): Unit = {
    if (node == null) return
    node.value = value
    values += value
    recover(node.left, 2 * value + 1)
    recover(node.right, 2 * value + 2)
  }
  recover(_root, 0)

  def find(target: Int): Boolean = values.contains(target)
}
