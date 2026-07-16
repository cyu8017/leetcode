// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

class Solution {
    fun findRightInterval(intervals: Array<IntArray>): IntArray {
        val indexed = intervals.mapIndexed { index, interval -> interval[0] to index }
            .sortedBy { it.first }
        val starts = indexed.map { it.first }.toIntArray()
        val result = IntArray(intervals.size)

        for (i in intervals.indices) {
            val end = intervals[i][1]
            var position = starts.binarySearch(end)
            if (position < 0) {
                position = -position - 1
            }
            result[i] = if (position == starts.size) -1 else indexed[position].second
        }

        return result
    }
}
