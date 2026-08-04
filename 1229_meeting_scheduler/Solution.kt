// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

class Solution {
    fun minAvailableDuration(slots1: Array<IntArray>, slots2: Array<IntArray>, duration: Int): List<Int> {
        slots1.sortBy { it[0] }
        slots2.sortBy { it[0] }
        var i = 0
        var j = 0
        while (i < slots1.size && j < slots2.size) {
            val start = maxOf(slots1[i][0], slots2[j][0])
            val end = minOf(slots1[i][1], slots2[j][1])
            if (end - start >= duration) return listOf(start, start + duration)
            if (slots1[i][1] < slots2[j][1]) i++ else j++
        }
        return emptyList()
    }
}
