// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private val g = scala.collection.mutable.Map.empty[TreeNode, Array[TreeNode]]
  private val vis = scala.collection.mutable.Map.empty[Int, Boolean]

  private def dfs(node: TreeNode, p: TreeNode): Unit = {
    if (node == null) return
    g(node) = Array(p, node.left, node.right)
    dfs(node.left, node)
    dfs(node.right, node)
  }

  private def dfs2(node: TreeNode): Int = {
    if (node == null || vis.getOrElse(node.value, false)) return 0
    vis(node.value) = true
    val res = node.value
    var best = 0
    g(node).foreach { nxt => best = math.max(best, dfs2(nxt)) }
    vis(node.value) = false
    res + best
  }

  def maxSum(root: TreeNode): Int = {
    g.clear()
    vis.clear()
    dfs(root, null)
    var ans = Int.MinValue
    g.keys.foreach { node =>
      ans = math.max(ans, dfs2(node))
      vis.clear()
    }
    ans
  }
}
