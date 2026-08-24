// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private var cur: TreeNode? = null

    fun increasingBST(root: TreeNode?): TreeNode? {
        val dummy = TreeNode(0)
        cur = dummy
        inorder(root)
        return dummy.right
    }

    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        node.left = null
        cur!!.right = node
        cur = node
        inorder(node.right)
    }
}
