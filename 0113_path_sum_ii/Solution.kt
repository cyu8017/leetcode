// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val paths = mutableListOf<List<Int>>()
        fun dfs(node: TreeNode?, remaining: Int, path: MutableList<Int>) {
            if (node == null) return
            path.add(node.`val`)
            if (node.left == null && node.right == null && node.`val` == remaining) {
                paths.add(path.toList())
            } else {
                dfs(node.left, remaining - node.`val`, path)
                dfs(node.right, remaining - node.`val`, path)
            }
            path.removeAt(path.lastIndex)
        }
        dfs(root, targetSum, mutableListOf())
        return paths
    }
}