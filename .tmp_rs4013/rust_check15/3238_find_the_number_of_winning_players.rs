struct Solution;
// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

use std::collections::HashSet;

impl Solution {
    pub fn winning_player_count(n: i32, pick: Vec<Vec<i32>>) -> i32 {
        let mut cnt = vec![[0; 11]; n as usize];
        let mut s = HashSet::new();
        for p in pick {
            let x = p[0] as usize;
            let y = p[1] as usize;
            cnt[x][y] += 1;
            if cnt[x][y] > x as i32 {
                s.insert(x);
            }
        }
        s.len() as i32
    }
}

fn main() {}
