// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun trimBST(root: TreeNode?, low: Int, high: Int): TreeNode? {
        if (root == null) return null
        if (root.`val` < low) return trimBST(root.right, low, high)
        if (root.`val` > high) return trimBST(root.left, low, high)
        root.left = trimBST(root.left, low, high)
        root.right = trimBST(root.right, low, high)
        return root
    }
}
