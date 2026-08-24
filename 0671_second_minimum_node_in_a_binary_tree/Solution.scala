// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def findSecondMinimumValue(root: TreeNode): Int = {
    if (root == null) return -1
    var ans = -1
    val rootVal = root.value
    def dfs(node: TreeNode): Unit = {
      if (node == null) return
      if (node.value > rootVal) {
        if (ans == -1 || node.value < ans) ans = node.value
        return
      }
      dfs(node.left)
      dfs(node.right)
    }
    dfs(root)
    ans
  }
}
