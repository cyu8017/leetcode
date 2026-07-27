// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findNearestRightNode(root: TreeNode?, u: TreeNode?): TreeNode? {
        val target = u?.`val` ?: return null
        var q = if (root != null) mutableListOf(root) else mutableListOf()
        while (q.isNotEmpty()) {
            val nxt = mutableListOf<TreeNode>()
            for (i in q.indices) {
                val node = q[i]
                if (node.`val` == target) {
                    return if (i + 1 < q.size) q[i + 1] else null
                }
                node.left?.let { nxt.add(it) }
                node.right?.let { nxt.add(it) }
            }
            q = nxt
        }
        return null
    }
}
