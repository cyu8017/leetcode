// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution {
    fun findMinimumTime(tasks: Array<IntArray>): Int {
        tasks.sortBy { it[1] }
        val on = BooleanArray(2001)
        for (t in tasks) {
            val start = t[0]
            val end = t[1]
            var duration = t[2]
            var have = 0
            for (i in start..end) if (on[i]) have += 1
            var i = end
            while (have < duration) {
                if (!on[i]) {
                    on[i] = true
                    have += 1
                }
                i -= 1
            }
        }
        return on.count { it }
    }
}
