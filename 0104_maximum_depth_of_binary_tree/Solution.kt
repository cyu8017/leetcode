// LeetCode 0104 - Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }
        return 1 + maxOf(maxDepth(root.left), maxDepth(root.right))
    }
}