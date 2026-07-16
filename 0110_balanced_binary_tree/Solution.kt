// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

import kotlin.math.abs
import kotlin.math.max

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isBalanced(root: TreeNode?): Boolean {
        return height(root) != -1
    }

    private fun height(node: TreeNode?): Int {
        if (node == null) {
            return 0
        }
        val left = height(node.left)
        if (left == -1) {
            return -1
        }
        val right = height(node.right)
        if (right == -1) {
            return -1
        }
        if (abs(left - right) > 1) {
            return -1
        }
        return 1 + max(left, right)
    }
}
