// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def averageOfSubtree(root: TreeNode): Int = {
    var ans = 0
    def dfs(node: TreeNode): Array[Int] = {
      if (node == null) return Array(0, 0)
      val L = dfs(node.left)
      val R = dfs(node.right)
      val sum = L(0) + R(0) + node.value
      val cnt = L(1) + R(1) + 1
      if (sum / cnt == node.value) ans += 1
      Array(sum, cnt)
    }
    dfs(root)
    ans
  }
}
