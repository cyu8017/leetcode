// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var hasPrev: Boolean = false
    private var prev: Int = 0
    private var best: Int = 0

    fun minDiffInBST(root: TreeNode?): Int {
        hasPrev = false
        best = Int.MAX_VALUE
        inorder(root)
        return best
    }

    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        if (hasPrev) best = minOf(best, node.`val` - prev)
        prev = node.`val`
        hasPrev = true
        inorder(node.right)
    }
}
