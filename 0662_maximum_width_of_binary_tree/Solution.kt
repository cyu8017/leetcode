// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun widthOfBinaryTree(root: TreeNode?): Int {
        if (root == null) return 0
        var best = 0
        val queue = ArrayDeque<Pair<TreeNode, Long>>()
        queue.add(root to 0L)
        while (queue.isNotEmpty()) {
            val size = queue.size
            val left = queue.first().second
            var right = left
            repeat(size) {
                val (node, idx) = queue.removeFirst()
                right = idx
                node.left?.let { queue.add(it to idx * 2) }
                node.right?.let { queue.add(it to idx * 2 + 1) }
            }
            best = maxOf(best, (right - left + 1).toInt())
        }
        return best
    }
}
