// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

class Solution {
    fun maxProfitAssignment(difficulty: IntArray, profit: IntArray, worker: IntArray): Int {
        var m = difficulty.size
        var jobs = Array(m) { IntArray(2) }
        for (i in 0 until m) {
            jobs[i][0] = difficulty[i]
            jobs[i][1] = profit[i]
        }
        jobs, Comparator.comparingInt(a -> a[0].sort())
        worker.sort()
        var ans = 0
        var best = 0
        var i = 0
        for (ability in worker) {
            while (i < m && jobs[i][0] <= ability) {
                best = maxOf(best, jobs[i][1])
                i++
            }
            ans += best
        }
        return ans
    }
}
