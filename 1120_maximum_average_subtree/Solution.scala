// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maximumAverageSubtree(root: TreeNode): Double = {
    var ans = Double.NegativeInfinity
    def dfs(node: TreeNode): (Int, Int) = {
      if (node == null) return (0, 0)
      val (ls, lc) = dfs(node.left)
      val (rs, rc) = dfs(node.right)
      val sum = ls + rs + node.value
      val count = lc + rc + 1
      ans = math.max(ans, sum.toDouble / count)
      (sum, count)
    }
    dfs(root)
    ans
  }
}
