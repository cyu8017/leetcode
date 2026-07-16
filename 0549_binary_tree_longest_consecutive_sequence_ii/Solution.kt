// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best = 0

    fun longestConsecutive(root: TreeNode?): Int {
        dfs(root)
        return best
    }

    private fun dfs(node: TreeNode?): Pair<Int, Int> {
        if (node == null) {
            return 0 to 0
        }

        val (leftInc, leftDec) = dfs(node.left)
        val (rightInc, rightDec) = dfs(node.right)

        var inc = 1
        var dec = 1

        node.left?.let { left ->
            when {
                left.`val` == node.`val` + 1 -> inc = maxOf(inc, leftInc + 1)
                left.`val` == node.`val` - 1 -> dec = maxOf(dec, leftDec + 1)
            }
        }
        node.right?.let { right ->
            when {
                right.`val` == node.`val` + 1 -> inc = maxOf(inc, rightInc + 1)
                right.`val` == node.`val` - 1 -> dec = maxOf(dec, rightDec + 1)
            }
        }

        if (node.left != null && node.right != null) {
            if (node.left!!.`val` + 1 == node.`val` && node.`val` == node.right!!.`val` - 1) {
                best = maxOf(best, leftDec + 1 + rightInc)
            }
            if (node.left!!.`val` - 1 == node.`val` && node.`val` == node.right!!.`val` + 1) {
                best = maxOf(best, leftInc + 1 + rightDec)
            }
        }

        best = maxOf(best, inc, dec)
        return inc to dec
    }
}
