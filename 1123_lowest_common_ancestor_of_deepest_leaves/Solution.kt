// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun lcaDeepestLeaves(root: TreeNode?): TreeNode? {
        fun dfs(node: TreeNode?): Pair<TreeNode?, Int> {
            if (node == null) return null to 0
            val (leftNode, leftDepth) = dfs(node.left)
            val (rightNode, rightDepth) = dfs(node.right)
            return when {
                leftDepth > rightDepth -> leftNode to leftDepth + 1
                rightDepth > leftDepth -> rightNode to rightDepth + 1
                else -> node to leftDepth + 1
            }
        }
        return dfs(root).first
    }
}
