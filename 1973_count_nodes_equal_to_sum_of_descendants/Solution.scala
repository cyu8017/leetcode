// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def equalToDescendants(root: TreeNode): Int = {
    var ans = 0
    def dfs(node: TreeNode): Long = {
      if (node == null) return 0L
      val total = dfs(node.left) + dfs(node.right)
      if (total == node.value) ans += 1
      total + node.value
    }
    dfs(root)
    ans
  }
}
