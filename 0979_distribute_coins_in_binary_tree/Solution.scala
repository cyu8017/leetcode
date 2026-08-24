// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def distributeCoins(root: TreeNode): Int = {
    var ans = 0
    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val left = dfs(node.left)
      val right = dfs(node.right)
      ans += math.abs(left) + math.abs(right)
      node.value + left + right - 1
    }
    dfs(root)
    ans
  }
}
