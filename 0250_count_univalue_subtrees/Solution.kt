// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var count = 0

    fun countUnivalSubtrees(root: TreeNode?): Int {
        count = 0
        dfs(root)
        return count
    }

    private fun dfs(node: TreeNode?): Boolean {
        if (node == null) {
            return true
        }
        val leftOk = dfs(node.left)
        val rightOk = dfs(node.right)
        if (!leftOk || !rightOk) {
            return false
        }
        if (node.left != null && node.left!!.`val` != node.`val`) {
            return false
        }
        if (node.right != null && node.right!!.`val` != node.`val`) {
            return false
        }
        count++
        return true
    }
}
