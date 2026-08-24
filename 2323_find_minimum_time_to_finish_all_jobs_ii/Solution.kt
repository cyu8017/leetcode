// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

class Solution {
    fun minimumTime(jobs: IntArray, workers: IntArray): Int {
        jobs.sort()
        workers.sort()
        var ans = 0
        for (i in jobs.indices) {
            ans = maxOf(ans, (jobs[i] + workers[i] - 1) / workers[i])
        }
        return ans
    }
}
