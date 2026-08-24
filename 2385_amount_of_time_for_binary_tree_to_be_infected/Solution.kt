// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

import java.util.ArrayDeque

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private val g = HashMap<Int, ArrayList<Int>>()

    fun amountOfTime(root: TreeNode?, start: Int): Int {
        build(root, null)
        var ans = 0
        val vis = HashSet<Int>()
        vis.add(start)
        val q = ArrayDeque<IntArray>()
        q.offer(intArrayOf(start, 0))
        while (q.isNotEmpty()) {
            val cur = q.poll()
            ans = maxOf(ans, cur[1])
            for (nxt in g.getOrDefault(cur[0], ArrayList())) {
                if (vis.add(nxt)) q.offer(intArrayOf(nxt, cur[1] + 1))
            }
        }
        return ans
    }

    private fun build(node: TreeNode?, parent: TreeNode?) {
        if (node == null) return
        if (parent != null) {
            g.getOrPut(node.`val`) { ArrayList() }.add(parent.`val`)
            g.getOrPut(parent.`val`) { ArrayList() }.add(node.`val`)
        }
        build(node.left, node)
        build(node.right, node)
    }
}
