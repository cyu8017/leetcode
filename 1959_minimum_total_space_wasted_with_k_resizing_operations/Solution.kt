// LeetCode 1959
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

class Solution {
    fun minSpaceWastedKResizing(nums: IntArray, k: Int): Int {
        val n = nums.size
        val inf = 1_000_000_000_000_000L
        val waste = Array(n) { LongArray(n) }
        for (i in 0 until n) {
            var mx = 0
            var total = 0L
            for (j in i until n) {
                mx = maxOf(mx, nums[j])
                total += nums[j]
                waste[i][j] = mx.toLong() * (j - i + 1) - total
            }
        }
        val segments = k + 1
        val dp = Array(n + 1) { LongArray(segments + 1) { inf } }
        dp[0][0] = 0
        for (i in 1..n) {
            for (s in 1..minOf(segments, i)) {
                for (p in s - 1 until i) {
                    dp[i][s] = minOf(dp[i][s], dp[p][s - 1] + waste[p][i - 1])
                }
            }
        }
        return (1..segments).minOf { dp[n][it] }.toInt()
    }
}
