// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        val result = mutableListOf<IntArray>()
        var i = 0
        val merged = newInterval.clone()

        while (i < intervals.size && intervals[i][1] < merged[0]) {
            result.add(intervals[i])
            i++
        }

        while (i < intervals.size && intervals[i][0] <= merged[1]) {
            merged[0] = minOf(merged[0], intervals[i][0])
            merged[1] = maxOf(merged[1], intervals[i][1])
            i++
        }

        result.add(merged)

        while (i < intervals.size) {
            result.add(intervals[i])
            i++
        }

        return result.toTypedArray()
    }
}
