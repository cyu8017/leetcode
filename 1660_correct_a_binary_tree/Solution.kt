// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun correctBinaryTree(root: TreeNode?): TreeNode? {
        val seen = HashSet<TreeNode>()
        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            if (node.right != null && node.right in seen) return null
            seen.add(node)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        }
        return dfs(root)
    }
}
