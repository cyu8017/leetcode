// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best = 0

    fun diameterOfBinaryTree(root: TreeNode?): Int {
        depth(root)
        return best
    }

    private fun depth(node: TreeNode?): Int {
        if (node == null) {
            return 0
        }
        val left = depth(node.left)
        val right = depth(node.right)
        best = maxOf(best, left + right)
        return 1 + maxOf(left, right)
    }
}
