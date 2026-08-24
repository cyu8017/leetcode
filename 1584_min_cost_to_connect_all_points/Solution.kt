// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

import kotlin.math.abs

class Solution {
    fun minCostConnectPoints(points: Array<IntArray>): Int {
        val n = points.size
        val used = BooleanArray(n)
        val dist = IntArray(n) { 1_000_000_000 }
        dist[0] = 0
        var answer = 0
        repeat(n) {
            var u = -1
            for (i in 0 until n) {
                if (!used[i] && (u == -1 || dist[i] < dist[u])) u = i
            }
            used[u] = true
            answer += dist[u]
            for (v in 0 until n) {
                if (!used[v]) {
                    val d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if (d < dist[v]) dist[v] = d
                }
            }
        }
        return answer
    }
}
