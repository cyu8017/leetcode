class TreeNode(var `val`: Int = 0, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun upsideDownBinaryTree(root: TreeNode?): TreeNode? {
        var previous: TreeNode? = null; var previousRight: TreeNode? = null; var current = root
        while (current != null) {
            val next = current.left
            current.left = previousRight
            previousRight = current.right
            current.right = previous
            previous = current
            current = next
        }
        return previous
    }
}