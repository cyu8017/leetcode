// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
    fun repairCars(ranks: IntArray, cars: Int): Long {
        var mn = Int.MAX_VALUE
        for (r in ranks) { if (r < mn) mn = r }
        var lo = 1
        var hi = mn * cars * cars
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (ok(ranks, cars, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(ranks: IntArray, cars: Int, t: Long): Boolean {
        var done = 0
        for (r in ranks) {
            var lo = 0
            var hi = cars
            while (lo < hi) {
                var mid = (lo + hi + 1) / 2
                if (r * mid * mid <= t) lo = mid
                else hi = mid - 1
            }
            done += lo
            if (done >= cars) return true
        }
        return done >= cars
    }
}
