// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

class Solution {
    fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
        intervals.sortBy { it[1] }
        var removed = 0
        var end = Int.MIN_VALUE
        for ((start, finish) in intervals) {
            if (start < end) {
                removed++
            } else {
                end = finish
            }
        }
        return removed
    }
}
