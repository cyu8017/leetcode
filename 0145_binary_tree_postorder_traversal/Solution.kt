// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode(var `val`: Int) { var left: TreeNode? = null; var right: TreeNode? = null }
class Solution {
    fun postorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        fun traverse(node: TreeNode?) {
            if (node == null) return
            traverse(node.left); traverse(node.right); result.add(node.`val`)
        }
        traverse(root)
        return result
    }
}