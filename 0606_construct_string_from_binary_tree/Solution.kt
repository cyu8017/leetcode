// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun tree2str(root: TreeNode?): String {
        if (root == null) return ""
        if (root.left == null && root.right == null) return root.`val`.toString()
        if (root.right == null) return root.`val`.toString() + "(" + tree2str(root.left) + ")"
        return root.`val`.toString() + "(" + tree2str(root.left) + ")(" + tree2str(root.right) + ")"
    }
}
