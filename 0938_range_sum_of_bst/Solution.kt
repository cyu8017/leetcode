// LeetCode 0938 - Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        if (root == null) return 0
        if (root.`val` < low) return rangeSumBST(root.right, low, high)
        if (root.`val` > high) return rangeSumBST(root.left, low, high)
        return root.`val` + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    }
}
