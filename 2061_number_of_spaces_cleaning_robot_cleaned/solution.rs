// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

use std::collections::HashSet;

impl Solution {
    pub fn number_of_clean_rooms(room: Vec<Vec<i32>>) -> i32 {
        let m = room.len() as i32;
        let n = room[0].len() as i32;
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut vis = HashSet::new();
        let mut cleaned = HashSet::new();
        cleaned.insert((0, 0));
        let mut r = 0;
        let mut c = 0;
        let mut d = 0;
        while vis.insert((r, c, d)) {
            let nr = r + dirs[d].0;
            let nc = c + dirs[d].1;
            if nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr as usize][nc as usize] == 0 {
                r = nr;
                c = nc;
                cleaned.insert((r, c));
            } else {
                d = (d + 1) % 4;
            }
        }
        cleaned.len() as i32
    }
}
