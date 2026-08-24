// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun printTree(root: TreeNode?): List<List<String>> {
        val height = height(root)
        val width = (1 shl height) - 1
        val result = List(height) { MutableList(width) { "" } }
        fun fill(node: TreeNode?, r: Int, left: Int, right: Int) {
            if (node == null) return
            val mid = (left + right) / 2
            result[r][mid] = node.`val`.toString()
            fill(node.left, r + 1, left, mid - 1)
            fill(node.right, r + 1, mid + 1, right)
        }
        fill(root, 0, 0, width - 1)
        return result
    }

    private fun height(node: TreeNode?): Int {
        if (node == null) return 0
        return 1 + maxOf(height(node.left), height(node.right))
    }
}
