// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

use std::collections::BTreeSet;

impl Solution {
    pub fn closest_room(rooms: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut rooms = rooms;
        rooms.sort_unstable_by_key(|room| room[1]);

        let mut indexed: Vec<(usize, i32, i32)> = queries
            .iter()
            .enumerate()
            .map(|(i, q)| (i, q[0], q[1]))
            .collect();
        indexed.sort_unstable_by(|a, b| b.2.cmp(&a.2));

        let mut available_ids = BTreeSet::new();
        let mut room_index = rooms.len() as i32 - 1;
        let mut answer = vec![-1; queries.len()];

        for (query_index, preferred, min_size) in indexed {
            while room_index >= 0 && rooms[room_index as usize][1] >= min_size {
                available_ids.insert(rooms[room_index as usize][0]);
                room_index -= 1;
            }
            if available_ids.is_empty() {
                continue;
            }

            let mut best_id = -1;
            let mut best_dist = i32::MAX;

            if let Some(&room_id) = available_ids.range(preferred..).next() {
                let dist = (room_id - preferred).abs();
                if dist < best_dist || (dist == best_dist && room_id < best_id) {
                    best_id = room_id;
                    best_dist = dist;
                }
            }
            if let Some(&room_id) = available_ids.range(..preferred).next_back() {
                let dist = (room_id - preferred).abs();
                if dist < best_dist || (dist == best_dist && room_id < best_id) {
                    best_id = room_id;
                }
            }
            answer[query_index] = best_id;
        }
        answer
    }
}
