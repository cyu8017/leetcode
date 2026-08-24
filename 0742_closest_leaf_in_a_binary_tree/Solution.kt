// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findClosestLeaf(root: TreeNode?, k: Int): Int {
        val graph = HashMap<Int, MutableList<Int>>()
        val leaves = HashSet<Int>()
        build(root, null, graph, leaves)
        val q = ArrayDeque<Int>()
        val seen = HashSet<Int>()
        seen.add(k)
        q.add(k)
        while (q.isNotEmpty()) {
            val value = q.removeFirst()
            if (leaves.contains(value)) return value
            val neighbors = graph[value] ?: continue
            for (neighbor in neighbors) {
                if (seen.add(neighbor)) q.add(neighbor)
            }
        }
        return -1
    }

    private fun build(
        node: TreeNode?,
        parent: TreeNode?,
        graph: MutableMap<Int, MutableList<Int>>,
        leaves: MutableSet<Int>
    ) {
        if (node == null) return
        graph.getOrPut(node.`val`) { ArrayList<Int>() }
        if (parent != null) {
            graph.getOrPut(parent.`val`) { ArrayList<Int>() }
            graph[node.`val`]!!.add(parent.`val`)
            graph[parent.`val`]!!.add(node.`val`)
        }
        if (node.left == null && node.right == null) leaves.add(node.`val`)
        build(node.right, node, graph, leaves)
        build(node.left, node, graph, leaves)
    }
}
