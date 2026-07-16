// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

class Solution {
    func canAttendMeetings(_ intervals: [[Int]]) -> Bool {
        let sorted = intervals.sorted { $0[0] < $1[0] }
        for index in 1..<sorted.count {
            if sorted[index][0] < sorted[index - 1][1] {
                return false
            }
        }
        return true
    }
}
