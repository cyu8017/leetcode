// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun binaryTreePaths(root: TreeNode?): List<String> {
        val result = mutableListOf<String>()
        dfs(root, mutableListOf(), result)
        return result
    }

    private fun dfs(node: TreeNode?, path: MutableList<String>, result: MutableList<String>) {
        if (node == null) {
            return
        }
        path.add(node.`val`.toString())
        if (node.left == null && node.right == null) {
            result.add(path.joinToString("->"))
        } else {
            dfs(node.left, path, result)
            dfs(node.right, path, result)
        }
        path.removeAt(path.lastIndex)
    }
}
