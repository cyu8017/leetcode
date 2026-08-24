// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var total = 0

    fun findTilt(root: TreeNode?): Int {
        total = 0
        subtreeSum(root)
        return total
    }

    private fun subtreeSum(node: TreeNode?): Int {
        if (node == null) return 0
        val left = subtreeSum(node.left)
        val right = subtreeSum(node.right)
        total += kotlin.math.abs(left - right)
        return node.`val` + left + right
    }
}
