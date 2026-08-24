// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

class Solution {
    private lateinit var adj: Array<MutableList<Int>>
    private lateinit var vals: IntArray
    private lateinit var ans: IntArray
    private lateinit var path: Array<ArrayDeque<IntArray>>

    fun getCoprimes(nums: IntArray, edges: Array<IntArray>): IntArray {
        val n = nums.size
        vals = nums
        adj = Array(n) { mutableListOf() }
        for (e in edges) {
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        }
        ans = IntArray(n) { -1 }
        path = Array(51) { ArrayDeque() }
        dfs(0, -1, 0)
        return ans
    }

    private fun dfs(node: Int, parent: Int, depth: Int) {
        var bestDepth = -1
        var bestNode = -1
        val v = vals[node]
        for (d in 1..50) {
            if (gcd(v, d) == 1 && path[d].isNotEmpty()) {
                val cand = path[d].last()
                if (cand[0] > bestDepth) {
                    bestDepth = cand[0]
                    bestNode = cand[1]
                }
            }
        }
        ans[node] = bestNode
        path[v].addLast(intArrayOf(depth, node))
        for (nxt in adj[node]) {
            if (nxt != parent) {
                dfs(nxt, node, depth + 1)
            }
        }
        path[v].removeLast()
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
