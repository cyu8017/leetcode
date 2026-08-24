// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun treeToDoublyList(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }

        var first: TreeNode? = null
        var last: TreeNode? = null

        fun inorder(node: TreeNode?) {
            if (node == null) {
                return
            }
            inorder(node.left)
            if (last != null) {
                last!!.right = node
                node.left = last
            } else {
                first = node
            }
            last = node
            inorder(node.right)
        }

        inorder(root)
        if (first != null && last != null) {
            first!!.left = last
            last!!.right = first
        }
        return first
    }
}
