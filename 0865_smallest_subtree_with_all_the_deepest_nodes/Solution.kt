// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode? {
        return dfs(root).node
    }

    private fun dfs(node: TreeNode?): Result {
        if (node == null) return Result(0, null)
        val left = dfs(node.left)
        val right = dfs(node.right)
        if (left.depth > right.depth) return Result(left.depth + 1, left.node)
        if (right.depth > left.depth) return Result(right.depth + 1, right.node)
        return Result(left.depth + 1, node)
    }

    private class Result(val depth: Int, val node: TreeNode?)
}
