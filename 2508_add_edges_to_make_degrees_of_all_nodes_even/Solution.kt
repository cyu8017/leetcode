// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution {
    fun isPossible(n: Int, edges: List<List<Int>>): Boolean {
        val deg = IntArray(n + 1)
        val adj = Array(n + 1) { HashSet<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            deg[u]++
            deg[v]++
            adj[u].add(v)
            adj[v].add(u)
        }
        val odd = ArrayList<Int>()
        for (i in 1..n) if (deg[i] % 2 == 1) odd.add(i)
        if (odd.isEmpty()) return true
        if (odd.size == 2) {
            val a = odd[0]
            val b = odd[1]
            if (b !in adj[a]) return true
            for (i in 1..n) {
                if (i != a && i != b && i !in adj[a] && i !in adj[b]) return true
            }
            return false
        }
        if (odd.size == 4) {
            val a = odd[0]
            val b = odd[1]
            val c = odd[2]
            val d = odd[3]
            return (b !in adj[a] && d !in adj[c]) ||
                (c !in adj[a] && d !in adj[b]) ||
                (d !in adj[a] && c !in adj[b])
        }
        return false
    }
}
