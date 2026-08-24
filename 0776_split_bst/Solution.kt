// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun splitBST(root: TreeNode?, target: Int): Array<TreeNode?> {
        if (root == null) return arrayOf(null, null)
        if (root.`val` <= target) {
            val parts = splitBST(root.right, target)
            root.right = parts[0]
            return arrayOf(root, parts[1])
        }
        val leftParts = splitBST(root.left, target)
        root.left = leftParts[1]
        return arrayOf(leftParts[0], root)
    }
}
