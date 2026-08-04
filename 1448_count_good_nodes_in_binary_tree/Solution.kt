// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun goodNodes(root: TreeNode?): Int {
        fun visit(node: TreeNode?, maximum: Int): Int {
            if (node == null) return 0
            val good = if (node.`val` >= maximum) 1 else 0
            val nextMax = maxOf(maximum, node.`val`)
            return good + visit(node.left, nextMax) + visit(node.right, nextMax)
        }
        return visit(root, Int.MIN_VALUE)
    }
}
