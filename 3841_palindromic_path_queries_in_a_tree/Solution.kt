// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

class Solution {
    private lateinit var bit: IntArray
    private var n = 0
    private lateinit var parent: IntArray
    private lateinit var depth: IntArray
    private lateinit var size: IntArray
    private lateinit var heavy: IntArray
    private lateinit var head: IntArray
    private lateinit var position: IntArray
    private lateinit var graph: Array<ArrayList<Int>>

    fun palindromicPathQueries(n: Int, edges: Array<IntArray>, s: String, queries: Array<String>): BooleanArray {
        this.n = n
        graph = Array(n) { ArrayList() }
        for (edge in edges) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }
        parent = IntArray(n)
        depth = IntArray(n)
        parent.fill(-2)
        parent[0] = -1
        val order = ArrayList<Int>()
        order.add(0)
        var i = 0
        while (i < order.size) {
            val u = order[i]
            for (v in graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.add(v)
                }
            }
            i++
        }
        size = IntArray(n)
        heavy = IntArray(n)
        heavy.fill(-1)
        for (ii in n - 1 downTo 0) {
            val u = order[ii]
            size[u] = 1
            for (v in graph[u]) {
                if (parent[v] == u) {
                    size[u] += size[v]
                    if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v
                }
            }
        }
        head = IntArray(n)
        position = IntArray(n)
        val stack = ArrayList<IntArray>()
        stack.add(intArrayOf(0, 0))
        var nextPosition = 0
        while (stack.isNotEmpty()) {
            val chain = stack.removeAt(stack.size - 1)
            var u = chain[0]
            while (u != -1) {
                head[u] = chain[1]
                position[u] = nextPosition++
                for (v in graph[u]) {
                    if (parent[v] == u && v != heavy[u]) stack.add(intArrayOf(v, v))
                }
                u = heavy[u]
            }
        }
        bit = IntArray(n + 1)
        val current = s.toCharArray()
        for (node in 0 until n) update(position[node], 1 shl (current[node] - 'a'))
        val answer = ArrayList<Boolean>()
        for (query in queries) {
            val parts = query.split(" ")
            val op = parts[0]
            val node = parts[1].toInt()
            if (op == "update") {
                val newCharacter = parts[2][0]
                val delta = (1 shl (current[node] - 'a')) xor (1 shl (newCharacter - 'a'))
                update(position[node], delta)
                current[node] = newCharacter
            } else {
                val other = parts[2].toInt()
                val mask = pathMask(node, other)
                answer.add((mask and (mask - 1)) == 0)
            }
        }
        val out = BooleanArray(answer.size)
        for (ii in answer.indices) out[ii] = answer[ii]
        return out
    }

    private fun update(index0: Int, value: Int) {
        var index = index0 + 1
        while (index <= n) {
            bit[index] = bit[index] xor value
            index += index and -index
        }
    }

    private fun prefix(index0: Int): Int {
        var index = index0
        var result = 0
        while (index > 0) {
            result = result xor bit[index]
            index -= index and -index
        }
        return result
    }

    private fun pathMask(u0: Int, v0: Int): Int {
        var u = u0
        var v = v0
        var result = 0
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) {
                val tmp = u; u = v; v = tmp
            }
            result = result xor prefix(position[u] + 1) xor prefix(position[head[u]])
            u = parent[head[u]]
        }
        if (position[u] > position[v]) {
            val tmp = u; u = v; v = tmp
        }
        return result xor prefix(position[v] + 1) xor prefix(position[u])
    }
}
