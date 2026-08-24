// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun convertBST(root: TreeNode?) {
        var running = 0

        fun reverseInorder(node: TreeNode?) {
            if (node == null) {
                return
            }
            reverseInorder(node.right)
            running += node.`val`
            node.`val` = running
            reverseInorder(node.left)
        }

        reverseInorder(root)
    }
}
