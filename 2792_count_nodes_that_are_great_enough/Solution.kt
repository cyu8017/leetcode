// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var ans: Int = 0
    private var k: Int = 0

    fun countGreatEnoughNodes(root: TreeNode?, k: Int): Int {
        this.k = k
        this.ans = 0
        dfs(root)
        return ans
    }

    private fun dfs(node: TreeNode?): MutableList<Int> {
        if (node == null) return ArrayList()
        var vals = ArrayList<Int>()
        vals.add(node.`val`)
        vals.addAll(dfs(node.left))
        vals.addAll(dfs(node.right))
        var smaller = 0
        for (v in vals) { if (v < node.`val`) smaller++ }
        if (smaller >= k) ans++
        return vals
    }
}
