// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun deepestLeavesSum(root: TreeNode?): Int {
        var level = listOf(root!!)
        var answer = 0
        while (level.isNotEmpty()) {
            answer = level.sumOf { it.`val` }
            level = level.flatMap { node -> listOfNotNull(node.left, node.right) }
        }
        return answer
    }
}
