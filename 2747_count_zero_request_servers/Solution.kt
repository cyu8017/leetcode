// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

class Solution {
    fun countServers(n: Int, logs: Array<IntArray>, x: Int, queries: IntArray): IntArray {
        logs.sortWith(compareBy { it[1] })
        val qs = Array(queries.size) { IntArray(2) }
        for (i in queries.indices) {
            qs[i][0] = queries[i]
            qs[i][1] = i
        }
        qs.sortWith(compareBy { it[0] })
        val ans = IntArray(queries.size)
        val cnt = HashMap<Int, Int>()
        var active = 0
        var l = 0
        var r = 0
        for (q in qs) {
            val t = q[0]
            val qi = q[1]
            while (r < logs.size && logs[r][1] <= t) {
                val id = logs[r][0]
                val c = cnt.getOrDefault(id, 0)
                if (c == 0) active++
                cnt[id] = c + 1
                r++
            }
            while (l < r && logs[l][1] < t - x) {
                val id = logs[l][0]
                val c = cnt[id]!! - 1
                cnt[id] = c
                if (c == 0) active--
                l++
            }
            ans[qi] = n - active
        }
        return ans
    }
}
