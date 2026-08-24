// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun heightOfTree(root: TreeNode?): Int {
        if (root == null) return -1
        return dfs(root)
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return -1
        if (node.left != null && node.left.right == node) return dfs(node.right) + 1
        if (node.right != null && node.right.left == node) return dfs(node.left) + 1
        return maxOf(dfs(node.left), dfs(node.right)) + 1
    }
}
