// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

class Solution {
    fun canAttendMeetings(intervals: Array<IntArray>): Boolean {
        intervals.sortBy { it[0] }
        for (index in 1 until intervals.size) {
            if (intervals[index][0] < intervals[index - 1][1]) {
                return false
            }
        }
        return true
    }
}
