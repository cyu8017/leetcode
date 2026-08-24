// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum_time_to_complete_all_deliveries/

class Solution {
    fun minimumTime(d: IntArray, r: IntArray): Long {
        var lo = 1L
        var hi = 8_000_000_000_000_000_000L
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            if (ok(mid, d, r)) hi = mid else lo = mid + 1
        }
        return lo
    }

    private fun ok(T: Long, d: IntArray, r: IntArray): Boolean {
        val w0 = T - T / r[0]
        val w1 = T - T / r[1]
        return w0 + w1 >= d[0] + d[1]
    }
}
