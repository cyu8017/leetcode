// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private var i = 0
    private lateinit var voyage: IntArray
    private val ans = mutableListOf<Int>()

    fun flipMatchVoyage(root: TreeNode?, voyage: IntArray): List<Int> {
        this.voyage = voyage
        return if (dfs(root)) ans else listOf(-1)
    }

    private fun dfs(node: TreeNode?): Boolean {
        if (node == null) return true
        if (node.`val` != voyage[i]) return false
        i++
        if (node.left != null && node.left!!.`val` != voyage[i]) {
            ans.add(node.`val`)
            return dfs(node.right) && dfs(node.left)
        }
        return dfs(node.left) && dfs(node.right)
    }
}
