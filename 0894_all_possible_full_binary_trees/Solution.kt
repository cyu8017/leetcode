// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private val memo = HashMap<Int, MutableList<TreeNode>>()

    fun allPossibleFBT(n: Int): List<TreeNode> = build(n)

    private fun build(nodes: Int): MutableList<TreeNode> {
        memo[nodes]?.let { return it }
        val res = mutableListOf<TreeNode>()
        if (nodes % 2 == 0) {
            memo[nodes] = res
            return res
        }
        if (nodes == 1) {
            res.add(TreeNode(0))
            memo[nodes] = res
            return res
        }
        var left = 1
        while (left < nodes) {
            val right = nodes - 1 - left
            for (L in build(left)) {
                for (R in build(right)) {
                    res.add(TreeNode(0, L, R))
                }
            }
            left += 2
        }
        memo[nodes] = res
        return res
    }
}
