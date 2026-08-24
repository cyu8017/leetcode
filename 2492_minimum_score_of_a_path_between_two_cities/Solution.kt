// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution {
    fun minScore(n: Int, roads: Array<IntArray>): Int {
        val g = Array(n + 1) { ArrayList<IntArray>() }
        for (r in roads) {
            g[r[0]].add(intArrayOf(r[1], r[2]))
            g[r[1]].add(intArrayOf(r[0], r[2]))
        }
        val vis = BooleanArray(n + 1)
        var ans = 1 shl 30
        val q = ArrayDeque<Int>()
        q.add(1)
        vis[1] = true
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            for (e in g[u]) {
                val v = e[0]
                val w = e[1]
                if (w < ans) ans = w
                if (!vis[v]) {
                    vis[v] = true
                    q.add(v)
                }
            }
        }
        return ans
    }
}
