// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var baseTime: IntArray

    fun finishTime(n: Int, edges: Array<IntArray>, baseTime: IntArray): Long {
        this.baseTime = baseTime
        g = Array(n) { ArrayList() }
        for (e in edges) g[e[0]].add(e[1])
        return dfs(0)
    }

    private fun dfs(i: Int): Long {
        if (g[i].isEmpty()) return baseTime[i].toLong()
        val INF = 1L shl 62
        var earliest = INF
        var latest = -INF
        for (j in g[i]) {
            val a = dfs(j)
            earliest = minOf(earliest, a)
            latest = maxOf(latest, a)
        }
        val ownDuration = (latest - earliest) + baseTime[i]
        return latest + ownDuration
    }
}
