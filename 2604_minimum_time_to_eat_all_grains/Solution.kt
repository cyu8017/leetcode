// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

class Solution {
    fun minimumTime(hens: IntArray, grains: IntArray): Int {
        hens.sort()
        grains.sort()
        var lo = 0
        var hi = 2_000_000_000
        while (lo < hi) {
            var mid = lo + (hi - lo) / 2
            if (ok(hens, grains, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(hens: IntArray, grains: IntArray, t: Int): Boolean {
        var j = 0
        for (h in hens) {
            if (j >= grains.size) return true
            if (grains[j] >= h) {
                while (j < grains.size && grains[j] - h <= t) { j = j + 1 }
            } else {
                if (h - grains[j] > t) return false
                var left = h - grains[j]
                var maxRight1 = t - 2 * left
                var maxRight2 = (t - left) / 2
                var reach = h
                if (maxRight1 > maxRight2) {
                    if (maxRight1 > 0) reach = h + maxRight1
                } else {
                    if (maxRight2 > 0) reach = h + maxRight2
                }
                while (j < grains.size && grains[j] <= reach) { j = j + 1 }
            }
        }
        return j >= grains.size
    }
}
