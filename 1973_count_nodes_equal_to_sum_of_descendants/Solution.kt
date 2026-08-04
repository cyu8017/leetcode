// LeetCode 1973
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun equalToDescendants(root: TreeNode?): Int {
        var ans = 0
        fun dfs(node: TreeNode?): Long {
            if (node == null) return 0L
            val total = dfs(node.left) + dfs(node.right)
            if (total == node.`val`.toLong()) ans++
            return total + node.`val`
        }
        dfs(root)
        return ans
    }
}
