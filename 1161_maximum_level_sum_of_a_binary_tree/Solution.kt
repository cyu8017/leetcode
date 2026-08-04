// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun maxLevelSum(root: TreeNode?): Int {
        val queue = ArrayDeque<TreeNode>()
        queue.add(root!!)
        var bestSum = Int.MIN_VALUE
        var bestLevel = 1
        var level = 1
        while (queue.isNotEmpty()) {
            var total = 0
            repeat(queue.size) {
                val node = queue.removeFirst()
                total += node.`val`
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            if (total > bestSum) {
                bestSum = total
                bestLevel = level
            }
            level++
        }
        return bestLevel
    }
}
