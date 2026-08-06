// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def btreeGameWinningMove(root: TreeNode, n: Int, x: Int): Boolean = {
    var leftCount = 0
    var rightCount = 0
    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val l = dfs(node.left)
      val r = dfs(node.right)
      if (node.value == x) {
        leftCount = l
        rightCount = r
      }
      l + r + 1
    }
    dfs(root)
    math.max(leftCount, math.max(rightCount, n - leftCount - rightCount - 1)) > n / 2
  }
}
