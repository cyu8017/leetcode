// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution {
    fun busyStudent(startTime: IntArray, endTime: IntArray, queryTime: Int): Int {
        var count = 0
        for (i in startTime.indices) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) count++
        }
        return count
    }
}
