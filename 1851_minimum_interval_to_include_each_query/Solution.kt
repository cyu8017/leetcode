// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

import java.util.PriorityQueue

class Solution {
    fun minInterval(intervals: Array<IntArray>, queries: IntArray): IntArray {
        intervals.sortBy { it[0] }
        val indexed = queries.withIndex().sortedBy { it.value }
        val heap = PriorityQueue<IntArray>(compareBy { it[0] })
        val answer = IntArray(queries.size) { -1 }
        var intervalIdx = 0
        for ((queryIdx, query) in indexed) {
            while (intervalIdx < intervals.size && intervals[intervalIdx][0] <= query) {
                val left = intervals[intervalIdx][0]
                val right = intervals[intervalIdx][1]
                heap.offer(intArrayOf(right - left + 1, right))
                intervalIdx++
            }
            while (heap.isNotEmpty() && heap.peek()[1] < query) {
                heap.poll()
            }
            if (heap.isNotEmpty()) {
                answer[queryIdx] = heap.peek()[0]
            }
        }
        return answer
    }
}
