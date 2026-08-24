// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/


class Solution {
    fun leastInterval(tasks: CharArray, n: Int): Int {
        val freq = IntArray(26)
        var maxFreq = 0
        for (t in tasks) {
            val i = t - 'A'
            freq[i]++
            maxFreq = maxOf(maxFreq, freq[i])
        }
        var maxCount = 0
        for (f in freq) if (f == maxFreq) maxCount++
        return maxOf(tasks.size, (maxFreq - 1) * (n + 1) + maxCount)
    }
}
