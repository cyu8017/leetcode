// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun twoSumBSTs(root1: TreeNode?, root2: TreeNode?, target: Int): Boolean {
        val values = mutableSetOf<Int>()
        val stack = ArrayDeque<TreeNode>()
        root1?.let { stack.addLast(it) }
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            values.add(node.`val`)
            node.left?.let { stack.addLast(it) }
            node.right?.let { stack.addLast(it) }
        }
        root2?.let { stack.addLast(it) }
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            if (target - node.`val` in values) return true
            node.left?.let { stack.addLast(it) }
            node.right?.let { stack.addLast(it) }
        }
        return false
    }
}
