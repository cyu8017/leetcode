// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private lateinit var sizes: ArrayList<Int>

    private fun dfs(node: TreeNode?): IntArray {
        if (node == null) return intArrayOf(0, 0, 1)
        val L = dfs(node.left)
        val R = dfs(node.right)
        val sz = L[1] + R[1] + 1
        val perf = L[2] == 1 && R[2] == 1 && L[0] == R[0]
        if (perf) sizes.add(sz)
        return intArrayOf(maxOf(L[0], R[0]) + 1, sz, if (perf) 1 else 0)
    }

    fun kthLargestPerfectSubtree(root: TreeNode?, k: Int): Int {
        sizes = ArrayList()
        dfs(root)
        sizes.sortDescending()
        if (k > sizes.size) return -1
        return sizes[k - 1]
    }
}
