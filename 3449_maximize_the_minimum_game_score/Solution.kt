// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution {
    fun maxScore(points: IntArray, m: Int): Long {
        var lo = 0
        var hi = 1e18
        while (lo < hi) {
            var mid = (lo + hi + 1) / 2
            if (ok(points, m, mid)) lo = mid
            else hi = mid - 1
        }
        return lo
    }

    private fun ok(points: IntArray, m: Int, mid: Long): Boolean {
        var need = 0
        var extra = 0
        for (p in points) {
            var req = (mid + p - 1) / p
            if (req > extra) {
                var visits = req - extra
                need += 2 * visits - 1
                extra = visits - 1
            } else {
                need += 1
                extra = 0
            }
            if (need > m) return false
        }
        return need <= m
    }
}
