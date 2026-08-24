// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

class Solution {
    fun minMeetingRooms(intervals: Array<IntArray>): Int {
        val starts = IntArray(intervals.size) { intervals[it][0] }.sortedArray()
        val ends = IntArray(intervals.size) { intervals[it][1] }.sortedArray()
        var rooms = 0
        var maxRooms = 0
        var startIndex = 0
        var endIndex = 0

        while (startIndex < starts.size) {
            if (starts[startIndex] < ends[endIndex]) {
                rooms += 1
                maxRooms = maxOf(maxRooms, rooms)
                startIndex += 1
            } else {
                rooms -= 1
                endIndex += 1
            }
        }

        return maxRooms
    }
}
