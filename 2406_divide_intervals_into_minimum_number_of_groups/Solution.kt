// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution {
    fun minGroups(intervals: Array<IntArray>): Int {
        val events = Array(intervals.size * 2) { IntArray(2) }
        var idx = 0
        for (it in intervals) {
            events[idx++] = intArrayOf(it[0], 1)
            events[idx++] = intArrayOf(it[1] + 1, -1)
        }
        events.sortWith(compareBy({ it[0] }, { it[1] }))
        var cur = 0
        var ans = 0
        for (e in events) {
            cur += e[1]
            ans = maxOf(ans, cur)
        }
        return ans
    }
}
