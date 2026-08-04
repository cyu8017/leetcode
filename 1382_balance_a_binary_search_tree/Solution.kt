// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun balanceBST(root: TreeNode?): TreeNode? {
        val nodes = mutableListOf<TreeNode>()
        fun walk(x: TreeNode?) {
            if (x == null) return
            walk(x.left)
            nodes.add(x)
            walk(x.right)
        }
        walk(root)
        fun build(l: Int, r: Int): TreeNode? {
            if (l >= r) return null
            val m = (l + r) / 2
            val x = nodes[m]
            x.left = build(l, m)
            x.right = build(m + 1, r)
            return x
        }
        return build(0, nodes.size)
    }
}
