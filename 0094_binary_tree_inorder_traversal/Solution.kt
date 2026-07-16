// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode(var al: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun inorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        val stack = ArrayDeque<TreeNode>()
        var current = root
        while (current != null || stack.isNotEmpty()) {
            while (current != null) {
                stack.addLast(current)
                current = current.left
            }
            current = stack.removeLast()
            result.add(current.al)
            current = current.right
        }
        return result
    }
}
