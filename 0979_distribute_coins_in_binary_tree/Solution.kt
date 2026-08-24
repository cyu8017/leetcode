// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private var ans: Int = 0

    fun distributeCoins(root: TreeNode?): Int {
        dfs(root)
        return ans
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        var left = dfs(node.left)
        var right = dfs(node.right)
        ans += kotlin.math.abs(left) + kotlin.math.abs(right)
        return node.`val` + left + right - 1
    }
}
