// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution {
    fun collectTheCoins(coins: IntArray, edges: Array<IntArray>): Int {
        val n = coins.size
        val g = Array(n) { HashSet<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val deg = IntArray(n) { g[it].size }
        val q = ArrayDeque<Int>()
        for (i in 0 until n) {
            if (deg[i] == 1 && coins[i] == 0) q.add(i)
        }
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            for (v in ArrayList(g[u])) {
                g[v].remove(u)
                deg[v] -= 1
                if (deg[v] == 1 && coins[v] == 0) q.add(v)
            }
            g[u].clear()
            deg[u] = 0
        }
        repeat(2) {
            val leaves = ArrayList<Int>()
            for (i in 0 until n) if (deg[i] == 1) leaves.add(i)
            for (u in leaves) {
                for (v in ArrayList(g[u])) {
                    g[v].remove(u)
                    deg[v] -= 1
                }
                g[u].clear()
                deg[u] = 0
            }
        }
        var remain = 0
        for (i in 0 until n) remain += g[i].size
        return remain
    }
}
