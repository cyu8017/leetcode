// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) {
            return true
        }
        return mirrors(root.left, root.right)
    }

    private fun mirrors(left: TreeNode?, right: TreeNode?): Boolean {
        if (left == null && right == null) {
            return true
        }
        if (left == null || right == null || left.`val` != right.`val`) {
            return false
        }
        return mirrors(left.left, right.right) && mirrors(left.right, right.left)
    }
}
