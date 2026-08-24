// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun averageOfLevels(root: TreeNode?): DoubleArray {
        val result = ArrayList<Double>()
        if (root == null) return DoubleArray(0)
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val size = queue.size
            var sum = 0.0
            repeat(size) {
                val node = queue.removeFirst()
                sum += node.`val`
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            result.add(sum / size)
        }
        return result.toDoubleArray()
    }
}
