// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun pseudoPalindromicPaths(root: TreeNode?): Int {
        fun dfs(node: TreeNode?, mask: Int): Int {
            if (node == null) return 0
            val next = mask xor (1 shl node.`val`)
            if (node.left == null && node.right == null) {
                return if (next and (next - 1) == 0) 1 else 0
            }
            return dfs(node.left, next) + dfs(node.right, next)
        }
        return dfs(root, 0)
    }
}
