// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution {
    fun maximizeWin(prizePositions: IntArray, k: Int): Int {
        var n = prizePositions.size
        var dp = IntArray(n + 1)
        var ans = 0
        var left = 0
        for (right in 0 until n) {
            while (prizePositions[right] - prizePositions[left] > k) { left = left + 1 }
            var cur = right - left + 1
            if (dp[left] + cur > ans) ans = dp[left] + cur
            var best = cur
            if (dp[right] > best) best = dp[right]
            dp[right + 1] = best
        }
        return ans
    }
}
