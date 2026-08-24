// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

import java.util.ArrayDeque

class Solution {
    fun maximumDetonation(bombs: Array<IntArray>): Int {
        val n = bombs.size
        val g = Array(n) { mutableListOf<Int>() }
        for (i in 0 until n) {
            val x1 = bombs[i][0].toLong()
            val y1 = bombs[i][1].toLong()
            val r1 = bombs[i][2].toLong()
            for (j in 0 until n) {
                if (i == j) continue
                val dx = bombs[j][0] - x1
                val dy = bombs[j][1] - y1
                if (dx * dx + dy * dy <= r1 * r1) g[i].add(j)
            }
        }
        var ans = 0
        for (i in 0 until n) {
            val vis = BooleanArray(n)
            val q = ArrayDeque<Int>()
            q.offer(i)
            vis[i] = true
            var cnt = 0
            while (q.isNotEmpty()) {
                val u = q.poll()
                cnt++
                for (v in g[u]) if (!vis[v]) {
                    vis[v] = true
                    q.offer(v)
                }
            }
            ans = maxOf(ans, cnt)
        }
        return ans
    }
}
