// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sumRootToLeaf(root: TreeNode?): Int = dfs(root, 0)

    private fun dfs(node: TreeNode?, value: Int): Int {
        if (node == null) return 0
        val v = value * 2 + node.`val`
        if (node.left == null && node.right == null) return v
        return dfs(node.left, v) + dfs(node.right, v)
    }
}
