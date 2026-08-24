// LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        if (root == null) {
            return result
        }

        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        var leftToRight = true

        while (queue.isNotEmpty()) {
            val size = queue.size
            val level = mutableListOf<Int>()
            repeat(size) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            if (!leftToRight) {
                level.reverse()
            }
            result.add(level)
            leftToRight = !leftToRight
        }

        return result
    }
}
