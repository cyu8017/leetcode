// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun longestConsecutive(root: TreeNode?): Int = dfs(root, null, 0)

    private fun dfs(node: TreeNode?, parent: TreeNode?, length: Int): Int {
        if (node == null) {
            return 0
        }
        val current = if (parent != null && parent.`val` + 1 == node.`val`) length + 1 else 1
        return maxOf(current, dfs(node.left, node, current), dfs(node.right, node, current))
    }
}
