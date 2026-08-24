// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isValidBST(root: TreeNode?): Boolean {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE)
    }

    private fun valid(node: TreeNode?, low: Long, high: Long): Boolean {
        if (node == null) {
            return true
        }
        val value = node.`val`.toLong()
        if (!(low < value && value < high)) {
            return false
        }
        return valid(node.left, low, value) && valid(node.right, value, high)
    }
}
