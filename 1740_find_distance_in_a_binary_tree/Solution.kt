// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findDistance(root: TreeNode?, p: Int, q: Int): Int {
        val graph = HashMap<Int, MutableList<Int>>()
        dfs(root, null, graph)
        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(p to 0)
        val seen = hashSetOf(p)
        while (queue.isNotEmpty()) {
            val (node, dist) = queue.removeFirst()
            if (node == q) {
                return dist
            }
            for (nei in graph.getValue(node)) {
                if (seen.add(nei)) {
                    queue.add(nei to dist + 1)
                }
            }
        }
        return -1
    }

    private fun dfs(node: TreeNode?, parent: TreeNode?, graph: HashMap<Int, MutableList<Int>>) {
        if (node == null) {
            return
        }
        graph.getOrPut(node.`val`) { mutableListOf() }
        if (parent != null) {
            graph.getValue(node.`val`).add(parent.`val`)
            graph.getValue(parent.`val`).add(node.`val`)
        }
        dfs(node.left, node, graph)
        dfs(node.right, node, graph)
    }
}
