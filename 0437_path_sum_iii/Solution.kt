// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        val prefixCounts = HashMap<Long, Int>()
        prefixCounts[0L] = 1
        return dfs(root, 0L, targetSum.toLong(), prefixCounts)
    }

    private fun dfs(
        node: TreeNode?,
        current: Long,
        targetSum: Long,
        prefixCounts: HashMap<Long, Int>,
    ): Int {
        if (node == null) {
            return 0
        }
        val updated = current + node.`val`
        var total = prefixCounts.getOrDefault(updated - targetSum, 0)
        prefixCounts[updated] = prefixCounts.getOrDefault(updated, 0) + 1
        total += dfs(node.left, updated, targetSum, prefixCounts)
        total += dfs(node.right, updated, targetSum, prefixCounts)
        prefixCounts[updated] = prefixCounts.getValue(updated) - 1
        return total
    }
}
