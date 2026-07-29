// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun maxAncestorDiff(root: TreeNode?): Int {
        val r = root!!
        return dfs(r, r.`val`, r.`val`)
    }

    private fun dfs(node: TreeNode?, lo: Int, hi: Int): Int {
        if (node == null) return hi - lo
        val nlo = minOf(lo, node.`val`)
        val nhi = maxOf(hi, node.`val`)
        return maxOf(dfs(node.left, nlo, nhi), dfs(node.right, nlo, nhi))
    }
}
