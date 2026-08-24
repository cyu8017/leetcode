// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun closestNodes(root: TreeNode?, queries: List<Int>): List<List<Int>> {
        val vals = ArrayList<Int>()
        inorder(root, vals)
        val ans = ArrayList<List<Int>>()
        for (q in queries) {
            val j = lowerBound(vals, q)
            val mx = if (j < vals.size) vals[j] else -1
            val mn = when {
                j < vals.size && vals[j] == q -> q
                j > 0 -> vals[j - 1]
                else -> -1
            }
            ans.add(listOf(mn, mx))
        }
        return ans
    }

    private fun inorder(node: TreeNode?, vals: MutableList<Int>) {
        if (node == null) return
        inorder(node.left, vals)
        vals.add(node.`val`)
        inorder(node.right, vals)
    }

    private fun lowerBound(vals: List<Int>, q: Int): Int {
        var lo = 0
        var hi = vals.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (vals[mid] < q) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
