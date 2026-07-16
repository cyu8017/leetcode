// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best = Int.MIN_VALUE

    fun maxPathSum(root: TreeNode?): Int {
        best = Int.MIN_VALUE
        gain(root)
        return best
    }

    private fun gain(node: TreeNode?): Int {
        if (node == null) return 0
        val left = maxOf(gain(node.left), 0)
        val right = maxOf(gain(node.right), 0)
        best = maxOf(best, node.`val` + left + right)
        return node.`val` + maxOf(left, right)
    }
}