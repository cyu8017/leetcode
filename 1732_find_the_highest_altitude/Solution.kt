// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var altitude = 0
        var best = 0
        for (change in gain) {
            altitude += change
            best = maxOf(best, altitude)
        }
        return best
    }
}
