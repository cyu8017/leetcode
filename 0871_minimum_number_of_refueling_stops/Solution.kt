// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution {
    fun minRefuelStops(target: Int, startFuel: Int, stations: Array<IntArray>): Int {
        val pq = PriorityQueue<Int>(compareByDescending { it })
        val all = Array(stations.size + 1) { if (it < stations.size) stations[it] else intArrayOf(target, 0) }
        var ans = 0
        var prev = 0
        var fuel = startFuel.toLong()
        for (st in all) {
            val pos = st[0]
            val gas = st[1]
            fuel -= (pos - prev).toLong()
            while (pq.isNotEmpty() && fuel < 0) {
                fuel += pq.poll()
                ans++
            }
            if (fuel < 0) return -1
            pq.offer(gas)
            prev = pos
        }
        return ans
    }
}
