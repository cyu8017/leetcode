// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution {
    fun minNumberOfSeconds(mountainHeight: Int, workerTimes: IntArray): Long {
        var lo = 0
        var hi = 1e18
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (ok(mid, mountainHeight, workerTimes)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(t: Long, mountainHeight: Int, workerTimes: IntArray): Boolean {
        var total = 0
        for (w in workerTimes) {
            var l = 0
            var h = mountainHeight
            while (l < h) {
                var mid = (l + h + 1) / 2
                if (w * mid * (mid + 1) / 2 <= t) l = mid
                else h = mid - 1
            }
            total += l
            if (total >= mountainHeight) return true
        }
        return total >= mountainHeight
    }
}
