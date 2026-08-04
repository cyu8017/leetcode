// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

class Solution {
    fun frogPosition(n: Int, edges: Array<IntArray>, t: Int, target: Int): Double {
        val g = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        fun dfs(u: Int, p: Int, time: Int, prob: Double): Double {
            val kids = g[u].filter { it != p }
            if (time == t || kids.isEmpty()) return if (u == target) prob else 0.0
            var sum = 0.0
            for (v in kids) sum += dfs(v, u, time + 1, prob / kids.size)
            return sum
        }
        return dfs(1, 0, 0, 1.0)
    }
}
