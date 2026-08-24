// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution {
    fun countSubTrees(n: Int, edges: Array<IntArray>, labels: String): IntArray {
        val graph = List(n) { mutableListOf<Int>() }
        for (edge in edges) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }
        val answer = IntArray(n)
        dfs(0, -1, graph, labels, answer)
        return answer
    }

    private fun dfs(node: Int, parent: Int, graph: List<MutableList<Int>>, labels: String, answer: IntArray): IntArray {
        val counts = IntArray(26)
        counts[labels[node] - 'a']++
        for (neighbor in graph[node]) {
            if (neighbor == parent) continue
            val child = dfs(neighbor, node, graph, labels, answer)
            for (i in 0 until 26) counts[i] += child[i]
        }
        answer[node] = counts[labels[node] - 'a']
        return counts
    }
}
