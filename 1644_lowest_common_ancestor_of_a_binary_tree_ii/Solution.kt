// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        var found = 0
        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            val left = dfs(node.left)
            val right = dfs(node.right)
            if (same(node, p) || same(node, q)) {
                found++
                return node
            }
            return if (left != null && right != null) node else left ?: right
        }
        val ans = dfs(root)
        return if (found == 2) ans else null
    }

    private fun same(a: TreeNode?, b: TreeNode?): Boolean {
        if (a == null || b == null) return false
        return a === b || a.`val` == b.`val`
    }
}
