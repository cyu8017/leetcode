// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution {
    fun minmaxGasDist(stations: IntArray, k: Int): Double {
        var lo = 0.0
        var hi = (stations[stations.size - 1] - stations[0]).toDouble()
        while (hi - lo > 1e-6) {
            val mid = (lo + hi) / 2.0
            if (can(stations, k, mid)) hi = mid
            else lo = mid
        }
        return hi
    }

    private fun can(stations: IntArray, k: Int, dist: Double): Boolean {
        var needed = 0
        for (i in 1 until stations.size) {
            needed += ((stations[i] - stations[i - 1]) / dist).toInt()
        }
        return needed <= k
    }
}
