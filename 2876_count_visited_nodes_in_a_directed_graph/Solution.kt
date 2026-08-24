// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

class Solution {
    private var edges: IntArray? = null
    private var ans: IntArray? = null
    private var state: IntArray? = null
    private var stack: MutableList<Int>? = null

    fun countVisitedNodes(edgesList: MutableList<Int>): IntArray {
        var n = edgesList.size
        edges = IntArray(n)
        for (i in 0 until n) { edges[i] = edgesList[i] }
        ans = IntArray(n)
        state = IntArray(n)
        stack = ArrayList()
        for (i in 0 until n) { if (state[i] == 0) dfs(i) }
        return ans
    }

    private fun dfs(u: Int) {
        state[u] = 1
        stack.add(u)
        var v = edges[u]
        if (state[v] == 0) dfs(v)
        else if (state[v] == 1) {
            var idx = stack.size - 1
            while (stack[idx] != v) idx--
            var cyc = stack.size - idx
            for (i in idx until stack.size) { ans[stack[i]] = cyc }
        }
        if (ans[u] == 0) ans[u] = ans[edges[u]] + 1
        state[u] = 2
        stack.removeAt(stack.size - 1)
    }
}
