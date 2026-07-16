// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun flatten(root: TreeNode?) {
        fun flattenTail(node: TreeNode?): TreeNode? {
            if (node == null) return null
            val leftTail = flattenTail(node.left)
            val rightTail = flattenTail(node.right)
            if (leftTail != null) {
                leftTail.right = node.right
                node.right = node.left
                node.left = null
            }
            return rightTail ?: leftTail ?: node
        }
        flattenTail(root)
    }
}