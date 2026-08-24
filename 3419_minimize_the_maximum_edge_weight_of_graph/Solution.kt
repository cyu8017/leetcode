// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

class Solution {
    fun minMaxWeight(n: Int, edges: Array<IntArray>, threshold: Int): Int {
        var lo = 1
        var hi = 1000001
        var ans = -1
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (ok(n, edges, mid)) {
                ans = mid
                hi = mid
            } else lo = mid + 1
        }
        return ans
    }

    private fun ok(n: Int, edges: Array<IntArray>, mid: Int): Boolean {
        var g = ArrayList<MutableList<Int>>()
        for (i in 0 until n) { g.add(ArrayList()) }
        for (e in edges) {
            if (e[2] <= mid) g[e[1]].add(e[0])
        }
        var vis = BooleanArray(n)
        var q = ArrayDeque<Int>()
        q.offer(0)
        vis[0] = true
        var cnt = 1
        while (!q.isEmpty()) {
            var u = q.poll()
            for (v in g[u]) {
                if (!vis[v]) {
                    vis[v] = true
                    cnt = cnt + 1
                    q.offer(v)
                }
            }
        }
        cnt = = n
        return cnt
    }
}
