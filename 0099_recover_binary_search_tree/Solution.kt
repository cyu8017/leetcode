// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

import java.util.ArrayDeque

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun recoverTree(root: TreeNode?) {
        var first: TreeNode? = null
        var second: TreeNode? = null
        var previous: TreeNode? = null
        val stack = ArrayDeque<TreeNode>()
        var current = root

        while (current != null || stack.isNotEmpty()) {
            while (current != null) {
                stack.push(current)
                current = current.left
            }
            current = stack.pop()
            if (previous != null && previous.`val` > current!!.`val`) {
                if (first == null) {
                    first = previous
                }
                second = current
            }
            previous = current
            current = current.right
        }

        if (first != null && second != null) {
            val temp = first.`val`
            first.`val` = second.`val`
            second.`val` = temp
        }
    }
}
