// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

class Solution {
    fun minProcessingTime(processorTime: MutableList<Int>, tasks: MutableList<Int>): Int {
        processorTime.sort()
        tasks.sortDescending()
        var ans = 0
        for (i in processorTime.indices) {
            val fin = processorTime[i] + tasks[i * 4]
            if (fin > ans) ans = fin
        }
        return ans
    }
}
