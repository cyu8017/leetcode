// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sumNumbers(root: TreeNode?): Int = dfs(root, 0)

    private fun dfs(node: TreeNode?, current: Int): Int {
        if (node == null) return 0
        val value = current * 10 + node.`val`
        if (node.left == null && node.right == null) return value
        return dfs(node.left, value) + dfs(node.right, value)
    }
}