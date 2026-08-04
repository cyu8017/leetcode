// LeetCode 1971
// https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        if (source == destination) return true
        val g = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val stack = ArrayDeque<Int>()
        val seen = BooleanArray(n)
        stack.add(source)
        seen[source] = true
        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            if (u == destination) return true
            for (v in g[u]) if (!seen[v]) {
                seen[v] = true
                stack.add(v)
            }
        }
        return false
    }
}
