// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {
        intervals.sort_by_key(|interval| interval[0]);
        for index in 1..intervals.len() {
            if intervals[index][0] < intervals[index - 1][1] {
                return false;
            }
        }
        true
    }
}
