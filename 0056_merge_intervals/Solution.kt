// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        intervals.sortBy { it[0] }
        val merged = mutableListOf(intervals[0].clone())

        for (i in 1 until intervals.size) {
            val current = intervals[i]
            val last = merged[merged.lastIndex]

            if (current[0] <= last[1]) {
                last[1] = maxOf(last[1], current[1])
            } else {
                merged.add(current.clone())
            }
        }

        return merged.toTypedArray()
    }
}
