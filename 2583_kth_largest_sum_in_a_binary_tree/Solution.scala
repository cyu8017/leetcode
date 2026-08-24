// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def kthLargestLevelSum(root: TreeNode, k: Int): Long = {
    if (root == null) return -1
    val sums = scala.collection.mutable.ArrayBuffer.empty[Long]
    val q = scala.collection.mutable.Queue[TreeNode](root)
    while (q.nonEmpty) {
      val sz = q.size
      var s = 0L
      var i = 0
      while (i < sz) {
        val node = q.dequeue()
        s += node.value
        if (node.left != null) q.enqueue(node.left)
        if (node.right != null) q.enqueue(node.right)
        i += 1
      }
      sums += s
    }
    val sorted = sums.sorted(Ordering[Long].reverse)
    if (k > sorted.length) -1 else sorted(k - 1)
  }
}
