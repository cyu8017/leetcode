// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode(var al: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun generateTrees(n: Int): List<TreeNode?> {
        if (n == 0) {
            return emptyList()
        }
        return build(1, n)
    }

    private fun build(start: Int, end: Int): List<TreeNode?> {
        if (start > end) {
            return listOf(null)
        }
        val trees = mutableListOf<TreeNode?>()
        for (rootVal in start..end) {
            val leftTrees = build(start, rootVal - 1)
            val rightTrees = build(rootVal + 1, end)
            for (left in leftTrees) {
                for (right in rightTrees) {
                    val root = TreeNode(rootVal)
                    root.left = left
                    root.right = right
                    trees.add(root)
                }
            }
        }
        return trees
    }
}
