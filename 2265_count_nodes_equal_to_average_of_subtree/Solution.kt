// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private var ans = 0

    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(0, 0)
        val L = dfs(node.left)
        val R = dfs(node.right)
        val sum = L[0] + R[0] + node.`val`
        val cnt = L[1] + R[1] + 1
        if (sum / cnt == node.`val`) ans++
        return intArrayOf(sum, cnt)
    }

    fun averageOfSubtree(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }
}
