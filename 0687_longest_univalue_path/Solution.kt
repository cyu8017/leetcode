// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best: Int = 0

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        var left = dfs(node.left)
        var right = dfs(node.right)
        var leftPath = node.left != null && node.left.`val` == if (node.`val`) left + 1 else 0
        var rightPath = node.right != null && node.right.`val` == if (node.`val`) right + 1 else 0
        best = maxOf(best, leftPath + rightPath)
        return maxOf(leftPath, rightPath)
    }

    fun longestUnivaluePath(root: TreeNode?): Int {
        best = 0
        dfs(root)
        return best
    }
}
