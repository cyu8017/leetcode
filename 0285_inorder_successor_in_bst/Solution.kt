// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun inorderSuccessor(root: TreeNode?, p: TreeNode): TreeNode? {
        p.right?.let { right ->
            var current: TreeNode? = right
            while (current?.left != null) {
                current = current.left
            }
            return current
        }

        var successor: TreeNode? = null
        var current = root
        while (current != null) {
            if (p.`val` < current.`val`) {
                successor = current
                current = current.left
            } else {
                current = current.right
            }
        }
        return successor
    }
}
