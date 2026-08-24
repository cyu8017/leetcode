// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findSecondMinimumValue(root: TreeNode?): Int {
        if (root == null) return -1
        val minVal = root.`val`
        var second = Long.MAX_VALUE
        fun dfs(node: TreeNode?) {
            if (node == null) return
            if (node.`val` > minVal && node.`val` < second) second = node.`val`.toLong()
            if (node.`val` == minVal) {
                dfs(node.left)
                dfs(node.right)
            }
        }
        dfs(root)
        return if (second == Long.MAX_VALUE) -1 else second.toInt()
    }
}
