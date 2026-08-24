// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    var ans = 0

    fun dfs(node: TreeNode?): Int {
        if (node == null) return Int.MIN_VALUE
        var l = dfs(node.left)
        var r = dfs(node.right)
        var mx = maxOf(maxOf(l, r), node.`val`)
        if (mx == node.`val`) ans++
        return mx
    }

    fun countDominantNodes(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }
}
