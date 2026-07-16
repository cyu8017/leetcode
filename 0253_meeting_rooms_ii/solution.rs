// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Vec<i32>>) -> i32 {
        let mut starts: Vec<i32> = intervals.iter().map(|interval| interval[0]).collect();
        let mut ends: Vec<i32> = intervals.iter().map(|interval| interval[1]).collect();
        starts.sort_unstable();
        ends.sort_unstable();

        let mut rooms = 0;
        let mut max_rooms = 0;
        let mut start_index = 0;
        let mut end_index = 0;

        while start_index < starts.len() {
            if starts[start_index] < ends[end_index] {
                rooms += 1;
                max_rooms = max_rooms.max(rooms);
                start_index += 1;
            } else {
                rooms -= 1;
                end_index += 1;
            }
        }

        max_rooms
    }
}
