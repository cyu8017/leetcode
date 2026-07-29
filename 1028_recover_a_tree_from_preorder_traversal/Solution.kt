// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun recoverFromPreorder(traversal: String): TreeNode? {
        val stack = ArrayDeque<TreeNode>()
        var i = 0
        val n = traversal.length
        while (i < n) {
            var depth = 0
            while (i < n && traversal[i] == '-') {
                depth++
                i++
            }
            var `val` = 0
            while (i < n && traversal[i].isDigit()) {
                `val` = `val` * 10 + (traversal[i++] - '0')
            }
            val node = TreeNode(`val`)
            while (stack.size > depth) stack.removeLast()
            if (stack.isNotEmpty()) {
                val parent = stack.last()
                if (parent.left == null) parent.left = node else parent.right = node
            }
            stack.addLast(node)
        }
        while (stack.size > 1) stack.removeLast()
        return stack.lastOrNull()
    }
}
