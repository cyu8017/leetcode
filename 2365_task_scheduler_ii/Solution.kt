// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

class Solution {
    fun taskSchedulerII(tasks: IntArray, space: Int): Long {
        val next = HashMap<Int, Long>()
        var day = 0L
        for (t in tasks) {
            day = maxOf(day, next.getOrDefault(t, 0L))
            day++
            next[t] = day + space
        }
        return day
    }
}
