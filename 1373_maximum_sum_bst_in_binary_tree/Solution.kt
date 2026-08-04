// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var ans = 0

    fun maxSumBST(root: TreeNode?): Int {
        ans = 0
        dfs(root)
        return ans
    }

    // isBST, min, max, sum
    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(1, Int.MAX_VALUE, Int.MIN_VALUE, 0)
        val left = dfs(node.left)
        val right = dfs(node.right)
        if (left[0] == 1 && right[0] == 1 && left[2] < node.`val` && node.`val` < right[1]) {
            val s = left[3] + right[3] + node.`val`
            ans = maxOf(ans, s)
            return intArrayOf(1, minOf(left[1], node.`val`), maxOf(right[2], node.`val`), s)
        }
        return intArrayOf(0, 0, 0, 0)
    }
}
