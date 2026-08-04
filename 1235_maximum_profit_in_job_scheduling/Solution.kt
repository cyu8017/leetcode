// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution {
    fun jobScheduling(startTime: IntArray, endTime: IntArray, profit: IntArray): Int {
        val n = startTime.size
        val jobs = Array(n) { i -> intArrayOf(endTime[i], startTime[i], profit[i]) }
        jobs.sortBy { it[0] }
        val ends = IntArray(n + 1)
        val dp = IntArray(n + 1)
        for (i in 0 until n) {
            val end = jobs[i][0]
            val start = jobs[i][1]
            val gain = jobs[i][2]
            val idx = upperBound(ends, start, i)
            ends[i + 1] = end
            dp[i + 1] = maxOf(dp[i], dp[idx] + gain)
        }
        return dp[n]
    }

    private fun upperBound(ends: IntArray, target: Int, limit: Int): Int {
        var lo = 0
        var hi = limit
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (ends[mid] <= target) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
