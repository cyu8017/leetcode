// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def smallestFromLeaf(root: TreeNode): String = {
    var best = "~"
    def dfs(node: TreeNode, path: String): Unit = {
      if (node == null) return
      val next = (('a' + node.value).toChar.toString) + path
      if (node.left == null && node.right == null) {
        if (next < best) best = next
        return
      }
      dfs(node.left, next)
      dfs(node.right, next)
    }
    dfs(root, "")
    best
  }
}
