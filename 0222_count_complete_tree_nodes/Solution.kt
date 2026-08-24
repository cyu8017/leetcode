// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun countNodes(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }
        val left = leftDepth(root)
        val right = rightDepth(root)
        if (left == right) {
            return (1 shl left) - 1
        }
        return 1 + countNodes(root.left) + countNodes(root.right)
    }

    private fun leftDepth(node: TreeNode?): Int {
        var depth = 0
        var current = node
        while (current != null) {
            depth++
            current = current.left
        }
        return depth
    }

    private fun rightDepth(node: TreeNode?): Int {
        var depth = 0
        var current = node
        while (current != null) {
            depth++
            current = current.right
        }
        return depth
    }
}
