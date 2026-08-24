// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun reverseOddLevels(root: TreeNode?): TreeNode? {
        if (root != null) dfs(root.left, root.right, 1)
        return root
    }

    private fun dfs(a: TreeNode?, b: TreeNode?, level: Int) {
        if (a == null || b == null) return
        if (level % 2 == 1) {
            val tmp = a.`val`
            a.`val` = b.`val`
            b.`val` = tmp
        }
        dfs(a.left, b.right, level + 1)
        dfs(a.right, b.left, level + 1)
    }
}
