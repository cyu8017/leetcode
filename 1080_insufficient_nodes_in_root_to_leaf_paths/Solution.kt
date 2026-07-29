// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sufficientSubset(root: TreeNode?, limit: Int): TreeNode? {
        return dfs(root, 0, limit)
    }

    private fun dfs(node: TreeNode?, pathSum: Int, limit: Int): TreeNode? {
        if (node == null) return null
        val sum = pathSum + node.`val`
        if (node.left == null && node.right == null) {
            return if (sum >= limit) node else null
        }
        node.left = dfs(node.left, sum, limit)
        node.right = dfs(node.right, sum, limit)
        if (node.left == null && node.right == null) return null
        return node
    }
}
