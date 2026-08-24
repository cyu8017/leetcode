// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun btreeGameWinningMove(root: TreeNode?, n: Int, x: Int): Boolean {
        var left = 0
        var right = 0
        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0
            val l = dfs(node.left)
            val r = dfs(node.right)
            if (node.`val` == x) {
                left = l
                right = r
            }
            return l + r + 1
        }
        dfs(root)
        return maxOf(left, right, n - left - right - 1) > n / 2
    }
}
