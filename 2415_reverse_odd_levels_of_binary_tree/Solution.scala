// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def reverseOddLevels(root: TreeNode): TreeNode = {
    if (root != null) dfs(root.left, root.right, 1)
    root
  }

  private def dfs(a: TreeNode, b: TreeNode, level: Int): Unit = {
    if (a == null || b == null) return
    if (level % 2 == 1) {
      val tmp = a.value
      a.value = b.value
      b.value = tmp
    }
    dfs(a.left, b.right, level + 1)
    dfs(a.right, b.left, level + 1)
  }
}
