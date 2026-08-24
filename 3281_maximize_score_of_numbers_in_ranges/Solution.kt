// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution {
    fun maxPossibleScore(start: IntArray, d: Int): Int {
        start.sort()
        var n = start.size
        var lo = 0
        var hi = start[n - 1] + d - start[0] + 1
        while (lo < hi) {
            var mid = (lo + hi + 1) / 2
            if (ok(start, d, mid)) lo = mid
            else hi = mid - 1
        }
        return lo
    }

    private fun ok(start: IntArray, d: Int, mid: Int): Boolean {
        var prev = start[0]
        for (i in 1 until start.size) {
            var need = prev + mid
            var cur = start[i]
            if (need > cur + d) return false
            prev =if (need > cur) need else cur
        }
        return true
    }
}
