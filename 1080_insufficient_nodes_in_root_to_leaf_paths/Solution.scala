// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def sufficientSubset(root: TreeNode, limit: Int): TreeNode = {
    def dfs(node: TreeNode, pathSum: Int): TreeNode = {
      if (node == null) return null
      val sum = pathSum + node.value
      if (node.left == null && node.right == null) {
        return if (sum >= limit) node else null
      }
      node.left = dfs(node.left, sum)
      node.right = dfs(node.right, sum)
      if (node.left == null && node.right == null) null else node
    }
    dfs(root, 0)
  }
}
