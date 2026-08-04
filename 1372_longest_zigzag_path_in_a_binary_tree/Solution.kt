// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var ans = 0

    fun longestZigZag(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }

    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(-1, -1)
        val l = dfs(node.left)
        val r = dfs(node.right)
        val a = l[1] + 1
        val b = r[0] + 1
        ans = maxOf(ans, a, b)
        return intArrayOf(a, b)
    }
}
