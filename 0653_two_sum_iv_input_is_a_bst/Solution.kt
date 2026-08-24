// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findTarget(root: TreeNode?, k: Int): Boolean {
        val seen = HashSet<Int>()
        fun dfs(node: TreeNode?): Boolean {
            if (node == null) return false
            if (k - node.`val` in seen) return true
            seen.add(node.`val`)
            return dfs(node.left) || dfs(node.right)
        }
        return dfs(root)
    }
}
