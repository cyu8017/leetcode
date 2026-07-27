// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isEvenOddTree(root: TreeNode?): Boolean {
        var q = if (root != null) mutableListOf(root) else return true
        var level = 0
        while (q.isNotEmpty()) {
            var prev = if (level % 2 == 0) Int.MIN_VALUE else Int.MAX_VALUE
            val nxt = mutableListOf<TreeNode>()
            for (node in q) {
                if (node.`val` % 2 == level % 2) return false
                if (level % 2 == 0 && node.`val` <= prev) return false
                if (level % 2 == 1 && node.`val` >= prev) return false
                prev = node.`val`
                node.left?.let { nxt.add(it) }
                node.right?.let { nxt.add(it) }
            }
            q = nxt
            level++
        }
        return true
    }
}
