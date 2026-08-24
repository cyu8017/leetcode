// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun pruneTree(root: TreeNode?): TreeNode? {
        if (root == null) return null
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
        if (root.`val` == 0 && root.left == null && root.right == null) return null
        return root
    }
}
