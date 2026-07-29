// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var total = 0

    fun bstToGst(root: TreeNode?): TreeNode? {
        total = 0
        reverseInorder(root)
        return root
    }

    private fun reverseInorder(node: TreeNode?) {
        if (node == null) return
        reverseInorder(node.right)
        total += node.`val`
        node.`val` = total
        reverseInorder(node.left)
    }
}
