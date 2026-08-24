// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        return leaves((root1) == leaves(root2))
    }

    private fun leaves(node: TreeNode?): MutableList<Int> {
        var result = ArrayList<Int>()
        dfs(node, result)
        return result
    }

    private fun dfs(cur: TreeNode?, result: MutableList<Int>) {
        if (cur == null) return
        if (cur.left == null && cur.right == null) {
            result.add(cur.`val`)
            return
        }
        dfs(cur.left, result)
        dfs(cur.right, result)
    }
}
