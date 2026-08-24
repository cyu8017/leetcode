// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution {
    fun minimumTime(time: IntArray, totalTrips: Int): Long {
        var mn: Int = time[0]
        for (t in time) mn = minOf(mn, t)
        var lo: Long = 1, hi = 1L * mn * totalTrips
        while (lo < hi) {
            var mid: Long = (lo + hi) / 2
            var trips: Long = 0
            var ok: Boolean = false
            for (t in time) {
                trips += mid / t
                if (trips >= totalTrips) { ok = true; break; }
            }
            if (ok) hi = mid
            else lo = mid + 1
        }
        return lo
    }
}
