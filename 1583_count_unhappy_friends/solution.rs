// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

use std::collections::HashMap;

impl Solution {
    pub fn unhappy_friends(n: i32, preferences: Vec<Vec<i32>>, pairs: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let rank: Vec<HashMap<i32, usize>> = preferences
            .iter()
            .map(|pref| {
                pref.iter()
                    .enumerate()
                    .map(|(i, &friend)| (friend, i))
                    .collect()
            })
            .collect();
        let mut partner = vec![0; n];
        for p in &pairs {
            partner[p[0] as usize] = p[1];
            partner[p[1] as usize] = p[0];
        }
        let mut unhappy = 0;
        for x in 0..n {
            let y = partner[x];
            let y_rank = rank[x][&y];
            if preferences[x][..y_rank].iter().any(|&u| {
                rank[u as usize][&(x as i32)] < rank[u as usize][&partner[u as usize]]
            }) {
                unhappy += 1;
            }
        }
        unhappy
    }
}
