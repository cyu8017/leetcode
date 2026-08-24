// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    var g = HashMap<TreeNode, MutableList<TreeNode>>()
    var vis = HashMap<Int, Boolean>()

    fun dfs(node: TreeNode?, p: TreeNode?) {
        if (node == null) return
        var nbrs = ArrayList<TreeNode>()
        nbrs.add(p)
        nbrs.add(node.left)
        nbrs.add(node.right)
        g[node] = nbrs
        dfs(node.left, node)
        dfs(node.right, node)
    }

    fun dfs2(node: TreeNode?): Int {
        if (node == null || (Boolean.TRUE == vis[node.`val`])) return 0
        vis[node.`val`] = true
        var res = node.`val`
        var best = 0
        for (nxt in g[node]) { best = maxOf(best, dfs2(nxt)) }
        vis[node.`val`] = false
        return res + best
    }

    fun maxSum(root: TreeNode?): Int {
        g.clear()
        vis.clear()
        dfs(root, null)
        var ans = Int.MIN_VALUE
        for (node in g.keys) {
            ans = maxOf(ans, dfs2(node))
            vis.clear()
        }
        return ans
    }
}
