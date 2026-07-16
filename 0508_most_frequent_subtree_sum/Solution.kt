// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findFrequentTreeSum(root: TreeNode?): IntArray {
        val counts = mutableMapOf<Int, Int>()
        subtreeSum(root, counts)
        if (counts.isEmpty()) {
            return intArrayOf()
        }
        val best = counts.values.maxOrNull() ?: 0
        return counts.filter { it.value == best }.keys.sorted().toIntArray()
    }

    private fun subtreeSum(node: TreeNode?, counts: MutableMap<Int, Int>): Int {
        if (node == null) {
            return 0
        }
        val total = node.`val` + subtreeSum(node.left, counts) + subtreeSum(node.right, counts)
        counts[total] = counts.getOrDefault(total, 0) + 1
        return total
    }
}
