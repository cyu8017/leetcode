// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution {
    private var signalSpeed: Int = 0
    private List<int[]>[] g

    private fun dfs(a: Int, fa: Int, ws: Int): Int {
        var cnt = if ((ws % signalSpeed == 0)) 1 else 0
        for (e in g[a]) {
            var b = e[0]
            var w = e[1]
            if (b != fa) cnt += dfs(b, a, ws + w)
        }
        return cnt
    }

    fun countPairsOfConnectableServers(edges: Array<IntArray>, signalSpeed: Int): IntArray {
        this.signalSpeed = signalSpeed
        var n = edges.size + 1
        @SuppressWarnings("unchecked")
        List<int[]>[] g = ArrayList[n]
        this.g = g
        for (i in 0 until n) { g[i] = ArrayList() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        var ans = IntArray(n)
        for (a in 0 until n) {
            var s = 0
            for (e in g[a]) {
                var t = dfs(e[0], a, e[1])
                ans[a] += s * t
                s += t
            }
        }
        return ans
    }
}
