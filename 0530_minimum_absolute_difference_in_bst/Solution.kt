// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getMinimumDifference(root: TreeNode?): Int {
        var best = Int.MAX_VALUE
        var previous: Int? = null
        inorder(root) { value ->
            if (previous != null) {
                best = minOf(best, value - previous!!)
            }
            previous = value
        }
        return best
    }

    private fun inorder(node: TreeNode?, visit: (Int) -> Unit) {
        if (node == null) {
            return
        }
        inorder(node.left, visit)
        visit(node.`val`)
        inorder(node.right, visit)
    }
}
