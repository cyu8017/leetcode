// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun largestValues(root: TreeNode?): List<Int> {
        if (root == null) {
            return emptyList()
        }
        val result = mutableListOf<Int>()
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            var levelMax = Int.MIN_VALUE
            repeat(queue.size) {
                val node = queue.removeFirst()
                levelMax = maxOf(levelMax, node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            result.add(levelMax)
        }
        return result
    }
}
