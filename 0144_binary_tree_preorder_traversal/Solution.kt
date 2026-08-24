// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode(var `val`: Int) { var left: TreeNode? = null; var right: TreeNode? = null }
class Solution {
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        fun traverse(node: TreeNode?) {
            if (node == null) return
            result.add(node.`val`); traverse(node.left); traverse(node.right)
        }
        traverse(root)
        return result
    }
}