// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def minimumLevel(root: TreeNode): Int = {
    val q = new java.util.ArrayDeque[TreeNode]()
    q.offer(root)
    var s = Long.MaxValue
    var ans = 0
    var level = 1
    while (!q.isEmpty) {
      var t = 0L
      var m = q.size()
      while (m > 0) {
        val node = q.poll()
        t += node.value
        if (node.left != null) q.offer(node.left)
        if (node.right != null) q.offer(node.right)
        m -= 1
      }
      if (s > t) {
        s = t
        ans = level
      }
      level += 1
    }
    ans
  }
}
