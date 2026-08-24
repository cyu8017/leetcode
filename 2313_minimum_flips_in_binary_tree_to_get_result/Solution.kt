// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun minimumFlips(root: TreeNode?, result: Boolean): Int {
        val res = dfs(root!!)
        return if (result) res[1] else res[0]
    }

    private fun dfs(node: TreeNode): IntArray {
        if (node.left == null && node.right == null) {
            return if (node.`val` == 0) intArrayOf(0, 1) else intArrayOf(1, 0)
        }
        if (node.`val` == 5) {
            val x = dfs(node.left!!)
            return intArrayOf(x[1], x[0])
        }
        val L = dfs(node.left!!)
        val R = dfs(node.right!!)
        val lf = L[0]; val lt = L[1]; val rf = R[0]; val rt = R[1]
        return when (node.`val`) {
            2 -> intArrayOf(lf + rf, minOf(lt + rt, lt + rf, lf + rt))
            3 -> intArrayOf(minOf(lf + rf, lf + rt, lt + rf), lt + rt)
            4 -> intArrayOf(minOf(lf + rf, lt + rt), minOf(lf + rt, lt + rf))
            else -> intArrayOf(0, 0)
        }
    }
}
