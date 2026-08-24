// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode {
    var len: Int = 0
    var `val`: Char = '\u0000'
    var left: RopeTreeNode? = null
    var right: RopeTreeNode? = null
}

class Solution {
    fun getKthCharacter(root: RopeTreeNode, k: Int): Char = dfs(root, k)

    private fun dfs(node: RopeTreeNode, kk: Int): Char {
        if (node.left == null && node.right == null) return node.`val`
        var leftLen = 0
        if (node.left != null) leftLen = if (node.left!!.len > 0) node.left!!.len else 1
        if (kk <= leftLen) return dfs(node.left!!, kk)
        return dfs(node.right!!, kk - leftLen)
    }
}
