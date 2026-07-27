// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findNearestRightNode(root: TreeNode, u: TreeNode): TreeNode = {
    if (root == null || u == null) return null
    var q = List(root)
    while (q.nonEmpty) {
      val nxt = scala.collection.mutable.ListBuffer.empty[TreeNode]
      var i = 0
      while (i < q.length) {
        val node = q(i)
        if (node.eq(u) || node.value == u.value) {
          return if (i + 1 < q.length) q(i + 1) else null
        }
        if (node.left != null) nxt += node.left
        if (node.right != null) nxt += node.right
        i += 1
      }
      q = nxt.toList
    }
    null
  }
}
