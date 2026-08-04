// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class DSU(n: Int) {
    private val parent = IntArray(n + 1) { it }
    var components = n

    fun find(x: Int): Int {
        var cur = x
        while (cur != parent[cur]) {
            parent[cur] = parent[parent[cur]]
            cur = parent[cur]
        }
        return cur
    }

    fun union(a: Int, b: Int): Boolean {
        var x = find(a)
        var y = find(b)
        if (x == y) return false
        parent[x] = y
        components--
        return true
    }
}

class Solution {
    fun maxNumEdgesToRemove(n: Int, edges: Array<IntArray>): Int {
        val alice = DSU(n)
        val bob = DSU(n)
        var used = 0
        for (edge in edges) {
            if (edge[0] == 3) {
                val merged = alice.union(edge[1], edge[2])
                bob.union(edge[1], edge[2])
                if (merged) used++
            }
        }
        for (edge in edges) {
            when (edge[0]) {
                1 -> if (alice.union(edge[1], edge[2])) used++
                2 -> if (bob.union(edge[1], edge[2])) used++
            }
        }
        return if (alice.components == 1 && bob.components == 1) edges.size - used else -1
    }
}
