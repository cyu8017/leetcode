// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def countGreatEnoughNodes(root: TreeNode, k: Int): Int = {
    var ans = 0
    def dfs(node: TreeNode): List[Int] = {
      if (node == null) return List.empty
      val vals = node.value :: (dfs(node.left) ++ dfs(node.right))
      val smaller = vals.count(_ < node.value)
      if (smaller >= k) ans += 1
      vals
    }
    dfs(root)
    ans
  }
}
