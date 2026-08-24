// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun addOneRow(root: TreeNode?, `val`: Int, depth: Int): TreeNode? {
        if (depth == 1) {
            val node = TreeNode(`val`)
            node.left = root
            return node
        }
        dfs(root, `val`, 1, depth)
        return root
    }

    private fun dfs(node: TreeNode?, value: Int, cur: Int, depth: Int) {
        if (node == null) return
        if (cur == depth - 1) {
            val left = TreeNode(value)
            left.left = node.left
            val right = TreeNode(value)
            right.right = node.right
            node.left = left
            node.right = right
            return
        }
        dfs(node.left, value, cur + 1, depth)
        dfs(node.right, value, cur + 1, depth)
    }
}
