// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution {
    fun minDays(bloomDay: IntArray, m: Int, k: Int): Int {
        if (m.toLong() * k > bloomDay.size) return -1
        fun possible(day: Int): Boolean {
            var bouquets = 0
            var run = 0
            for (x in bloomDay) {
                run = if (x <= day) run + 1 else 0
                if (run == k) {
                    bouquets++
                    run = 0
                }
            }
            return bouquets >= m
        }
        var lo = bloomDay.minOrNull()!!
        var hi = bloomDay.maxOrNull()!!
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (possible(mid)) hi = mid else lo = mid + 1
        }
        return lo
    }
}
