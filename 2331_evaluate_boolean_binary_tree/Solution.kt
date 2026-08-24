// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun evaluateTree(root: TreeNode?): Boolean {
        val node = root!!
        if (node.left == null && node.right == null) return node.`val` == 1
        val l = evaluateTree(node.left)
        val r = evaluateTree(node.right)
        return if (node.`val` == 2) l || r else l && r
    }
}
