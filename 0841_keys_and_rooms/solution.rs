// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

use std::collections::HashSet;

impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let mut seen = HashSet::from([0]);
        let mut stack = vec![0];
        while let Some(room) = stack.pop() {
            for &key in &rooms[room] {
                if seen.insert(key as usize) {
                    stack.push(key as usize);
                }
            }
        }
        seen.len() == rooms.len()
    }
}
