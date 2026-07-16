// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

class Solution {
    func minMeetingRooms(_ intervals: [[Int]]) -> Int {
        let starts = intervals.map { $0[0] }.sorted()
        let ends = intervals.map { $0[1] }.sorted()
        var rooms = 0
        var maxRooms = 0
        var startIndex = 0
        var endIndex = 0

        while startIndex < starts.count {
            if starts[startIndex] < ends[endIndex] {
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                startIndex += 1
            } else {
                rooms -= 1
                endIndex += 1
            }
        }

        return maxRooms
    }
}
