// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def zigzagLevelSum(root: TreeNode): Array[Long] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Long]
    var q = scala.collection.mutable.ArrayBuffer[TreeNode](root)
    var left = true
    while (q.nonEmpty) {
      val nq = scala.collection.mutable.ArrayBuffer.empty[TreeNode]
      q.foreach { node =>
        if (node.left != null) nq += node.left
        if (node.right != null) nq += node.right
      }
      val m = q.length
      var s = 0L
      var i = 0
      var stop = false
      while (i < m && !stop) {
        val node = if (left) q(i) else q(m - i - 1)
        val child = if (left) node.left else node.right
        if (child == null) stop = true
        else s += node.value
        i += 1
      }
      ans += s
      left = !left
      q = nq
    }
    ans.toArray
  }
}
