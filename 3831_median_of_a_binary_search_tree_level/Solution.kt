// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var nums: MutableList<Int>? = null

    fun levelMedian(root: TreeNode?, level: Int): Int {
        nums = ArrayList()
        dfs(root, 0, level)
        if (nums.isEmpty()) return -1
        return nums[nums.size / 2]
    }

    private fun dfs(node: TreeNode?, i: Int, level: Int) {
        if (node == null) return
        dfs(node.left, i + 1, level)
        if (i == level) nums.add(node.`val`)
        dfs(node.right, i + 1, level)
    }
}
