// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def subtreeWithAllDeepest(root: TreeNode): TreeNode = {
    def dfs(node: TreeNode): (Int, TreeNode) = {
      if (node == null) return (0, null)
      val (ld, ln) = dfs(node.left)
      val (rd, rn) = dfs(node.right)
      if (ld > rd) (ld + 1, ln)
      else if (rd > ld) (rd + 1, rn)
      else (ld + 1, node)
    }
    dfs(root)._2
  }
}
