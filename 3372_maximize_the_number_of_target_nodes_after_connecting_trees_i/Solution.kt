// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

class Solution {
    private fun buildTree(n: Int, edges: Array<IntArray>): Array<ArrayList<Int>> {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        return g
    }

    private fun countWithin(g: Array<ArrayList<Int>>, start: Int, k: Int): Int {
        if (k < 0) return 0
        val n = g.size
        val vis = BooleanArray(n)
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(start, 0))
        vis[start] = true
        var cnt = 0
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val u = cur[0]
            val d = cur[1]
            cnt++
            if (d == k) continue
            for (v in g[u]) {
                if (!vis[v]) {
                    vis[v] = true
                    q.add(intArrayOf(v, d + 1))
                }
            }
        }
        return cnt
    }

    fun maxTargetNodes(edges1: Array<IntArray>, edges2: Array<IntArray>, k: Int): IntArray {
        val n = edges1.size + 1
        val m = edges2.size + 1
        val g1 = buildTree(n, edges1)
        val g2 = buildTree(m, edges2)
        val cnt1 = IntArray(n)
        for (i in 0 until n) cnt1[i] = countWithin(g1, i, k)
        var best2 = 0
        if (k > 0) {
            for (i in 0 until m) {
                val c = countWithin(g2, i, k - 1)
                if (c > best2) best2 = c
            }
        }
        val ans = IntArray(n)
        for (i in 0 until n) ans[i] = cnt1[i] + best2
        return ans
    }
}
