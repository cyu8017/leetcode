// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    fun distanceBetweenBusStops(distance: IntArray, start: Int, destination: Int): Int {
        var s = start
        var d = destination
        if (s > d) {
            val t = s; s = d; d = t
        }
        var clockwise = 0
        var total = 0
        for (i in distance.indices) {
            total += distance[i]
            if (i in s until d) clockwise += distance[i]
        }
        return minOf(clockwise, total - clockwise)
    }
}
