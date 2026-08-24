// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        intervals.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })
        var answer = 0
        var farthest = -1
        for (interval in intervals) {
            if (interval[1] > farthest) {
                answer++
                farthest = interval[1]
            }
        }
        return answer
    }
}
