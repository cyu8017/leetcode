// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution {
    fun maxRunTime(n: Int, batteries: IntArray): Long {
        var sum: Long = 0
        for (b in batteries) sum += b
        var lo: Long = 1, hi = sum / n
        while (lo < hi) {
            var mid: Long = (lo + hi + 1) / 2
            var need: Long = 0
            for (b in batteries) need += minOf(b, mid)
            if (need >= mid * n) lo = mid
            else hi = mid - 1
        }
        return lo
    }
}
