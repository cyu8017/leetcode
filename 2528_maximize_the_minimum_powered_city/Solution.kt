// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
    fun maxPower(stations: IntArray, r: Int, k: Int): Long {
        var n = stations.size
        var diff = LongArray(n + 1)
        for (i in 0 until n) {
            var L = maxOf(0, i - r)
            var R = minOf(n - 1, i + r)
            diff[L] += stations[i]
            diff[R + 1] -= stations[i]
        }
        var power = LongArray(n)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            power[i] = cur
        }
        var lo = 0
        var hi = k
        for (p in power) { if (p > hi) hi = p }
        hi += k
        while (lo < hi) {
            var mid = (lo + hi + 1) / 2
            if (ok(power, r, k, mid)) lo = mid
            else hi = mid - 1
        }
        return lo
    }

    private fun ok(power: LongArray, r: Int, k: Long, x: Long): Boolean {
        var n = power.size
        var extra = LongArray(n + 1)
        var have = 0
        var used = 0
        for (i in 0 until n) {
            have += extra[i]
            var need = x - (power[i] + have)
            if (need > 0) {
                used += need
                if (used > k) return false
                have += need
                var end = i + 2 * r
                if (end + 1 <= n) extra[end + 1] -= need
            }
        }
        return true
    }
}
