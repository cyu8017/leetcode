// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution {
    fun minSpeedOnTime(dist: IntArray, hour: Double): Int {
        val n = dist.size
        if (n - 1 >= hour) return -1
        fun canArrive(speed: Int): Boolean {
            var time = 0.0
            for (i in 0 until n - 1) {
                time += ((dist[i] + speed - 1) / speed).toDouble()
            }
            time += dist[n - 1].toDouble() / speed
            return time <= hour
        }
        if (!canArrive(10_000_000)) return -1
        var lo = 1
        var hi = 10_000_000
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (canArrive(mid)) hi = mid else lo = mid + 1
        }
        return lo
    }
}
