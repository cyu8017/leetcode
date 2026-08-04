// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best = 0.0

    fun maximumAverageSubtree(root: TreeNode?): Double {
        best = 0.0
        dfs(root)
        return best
    }

    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(0, 0)
        val left = dfs(node.left)
        val right = dfs(node.right)
        val sum = left[0] + right[0] + node.`val`
        val count = left[1] + right[1] + 1
        best = maxOf(best, sum.toDouble() / count)
        return intArrayOf(sum, count)
    }
}
