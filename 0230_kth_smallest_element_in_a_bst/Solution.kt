// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun kthSmallest(root: TreeNode?, k: Int): Int {
        val stack = ArrayDeque<TreeNode>()
        var current = root
        var remaining = k

        while (current != null || stack.isNotEmpty()) {
            while (current != null) {
                stack.addLast(current)
                current = current.left
            }
            current = stack.removeLast()
            remaining--
            if (remaining == 0) {
                return current!!.`val`
            }
            current = current.right
        }

        return -1
    }
}
