// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
    fun shipWithinDays(weights: IntArray, days: Int): Int {
        var lo = 0; var hi = 0
        for (w in weights) {
            lo = maxOf(lo, w)
            hi += w
        }
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (can(weights, days, mid)) hi = mid else lo = mid + 1
        }
        return lo
    }

    private fun can(weights: IntArray, days: Int, cap: Int): Boolean {
        var need = 1; var cur = 0
        for (w in weights) {
            if (cur + w > cap) {
                need++
                cur = 0
            }
            cur += w
        }
        return need <= days
    }
}
