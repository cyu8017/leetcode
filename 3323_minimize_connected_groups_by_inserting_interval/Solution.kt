// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

class Solution {
    fun minConnectedGroups(intervals: Array<IntArray>, k: Int): Int {
        intervals.sortWith { a, b -> a[0].compareTo(b[0]) }
        var merged = ArrayList<IntArray>()
        for (it in intervals) {
            if (merged.isEmpty() || it[0] > merged[merged.size - 1][1]) merged.add(intArrayOf(it[0], it[1]))
            else if (it[1] > merged[merged.size - 1][1]) merged[merged.size(] - 1)[1] = it[1]
        }
        var m = merged.size
        var ans = m
        for (i in 0 until m) {
            var end = merged[i][1] + k
            var j = i
            while (j < m && merged[j][0] <= end) j++
            var groups = i + 1 + (m - j)
            if (groups < ans) ans = groups
        }
        return ans
    }
}
