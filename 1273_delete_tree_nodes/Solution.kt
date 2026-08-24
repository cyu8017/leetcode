// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

class Solution {
    fun deleteTreeNodes(nodes: Int, parent: IntArray, value: IntArray): Int {
        val children = Array(nodes) { mutableListOf<Int>() }
        for (node in 1 until nodes) children[parent[node]].add(node)
        return dfs(0, children, value)[1]
    }

    private fun dfs(node: Int, children: Array<MutableList<Int>>, value: IntArray): IntArray {
        var total = value[node]
        var count = 1
        for (child in children[node]) {
            val result = dfs(child, children, value)
            total += result[0]
            count += result[1]
        }
        return intArrayOf(total, if (total == 0) 0 else count)
    }
}
