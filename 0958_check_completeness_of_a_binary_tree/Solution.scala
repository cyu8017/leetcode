// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def isCompleteTree(root: TreeNode): Boolean = {
    val q = scala.collection.mutable.Queue[TreeNode]()
    q.enqueue(root)
    var end = false
    while (q.nonEmpty) {
      val node = q.dequeue()
      if (node == null) end = true
      else {
        if (end) return false
        q.enqueue(node.left)
        q.enqueue(node.right)
      }
    }
    true
  }
}
