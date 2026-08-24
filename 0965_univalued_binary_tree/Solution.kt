// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    fun isUnivalTree(root: TreeNode?): Boolean {
        if (root == null) return true
        return dfs(root, root.`val`)
    }

    private fun dfs(node: TreeNode?, v: Int): Boolean {
        if (node == null) return true
        if (node.`val` != v) return false
        return dfs(node.left, v) && dfs(node.right, v)
    }
}
