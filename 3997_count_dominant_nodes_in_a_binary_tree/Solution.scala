// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private var ans = 0

  private def dfs(node: TreeNode): Int = {
    if (node == null) return Int.MinValue
    val l = dfs(node.left)
    val r = dfs(node.right)
    val mx = math.max(math.max(l, r), node.value)
    if (mx == node.value) ans += 1
    mx
  }

  def countDominantNodes(root: TreeNode): Int = {
    ans = 0
    dfs(root)
    ans
  }
}
