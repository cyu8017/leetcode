// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun deleteNode(root: TreeNode?, key: Int): TreeNode? {
        if (root == null) {
            return null
        }
        when {
            key < root.`val` -> root.left = deleteNode(root.left, key)
            key > root.`val` -> root.right = deleteNode(root.right, key)
            else -> {
                if (root.left == null) {
                    return root.right
                }
                if (root.right == null) {
                    return root.left
                }
                var successor = root.right!!
                while (successor.left != null) {
                    successor = successor.left!!
                }
                root.`val` = successor.`val`
                root.right = deleteNode(root.right, successor.`val`)
            }
        }
        return root
    }
}
