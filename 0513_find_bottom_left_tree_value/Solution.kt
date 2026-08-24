// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findBottomLeftValue(root: TreeNode): Int {
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        var leftmost = root.`val`
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            repeat(levelSize) { index ->
                val node = queue.removeFirst()
                if (index == 0) {
                    leftmost = node.`val`
                }
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
        }
        return leftmost
    }
}
