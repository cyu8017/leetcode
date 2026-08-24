// LeetCode 0617 - Merge Two Binary Trees
// https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun mergeTrees(root1: TreeNode?, root2: TreeNode?): TreeNode? {
        if (root1 == null) return root2
        if (root2 == null) return root1
        val node = TreeNode(root1.`val` + root2.`val`)
        node.left = mergeTrees(root1.left, root2.left)
        node.right = mergeTrees(root1.right, root2.right)
        return node
    }
}
