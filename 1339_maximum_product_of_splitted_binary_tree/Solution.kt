// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private val sums = mutableListOf<Long>()

    fun maxProduct(root: TreeNode?): Int {
        sums.clear()
        val whole = total(root)
        var best = 0L
        for (value in sums) {
            best = maxOf(best, value * (whole - value))
        }
        return (best % 1_000_000_007L).toInt()
    }

    private fun total(node: TreeNode?): Long {
        if (node == null) return 0
        val value = node.`val` + total(node.left) + total(node.right)
        sums.add(value)
        return value
    }
}
