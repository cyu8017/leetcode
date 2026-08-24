// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def evaluateTree(root: TreeNode): Boolean = {
    if (root.left == null && root.right == null) return root.value == 1
    val l = evaluateTree(root.left)
    val r = evaluateTree(root.right)
    if (root.value == 2) l || r else l && r
  }
}
