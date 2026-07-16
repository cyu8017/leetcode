// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
    var parent: Node? = null
}

class Solution {
    fun inorderSuccessor(node: Node): Node? {
        node.right?.let { right ->
            var current = right
            while (current.left != null) {
                current = current.left!!
            }
            return current
        }
        var current: Node? = node
        while (current?.parent != null && current === current.parent?.right) {
            current = current.parent
        }
        return current?.parent
    }
}
