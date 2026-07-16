// LeetCode 0111 - Minimum Depth of Binary Tree
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun minDepth(root: TreeNode?): Int {
        if (root == null) return 0
        if (root.left == null) return 1 + minDepth(root.right)
        if (root.right == null) return 1 + minDepth(root.left)
        return 1 + minOf(minDepth(root.left), minDepth(root.right))
    }
}