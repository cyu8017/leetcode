// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, nodes: Array<TreeNode?>): TreeNode? {
        val targets = nodes.filterNotNull().toHashSet()
        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            val l = dfs(node.left)
            val r = dfs(node.right)
            if (node in targets || (l != null && r != null)) return node
            return l ?: r
        }
        return dfs(root)
    }
}
