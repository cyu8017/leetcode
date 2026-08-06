// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

use std::collections::HashMap;

impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        let m = votes[0].len();
        let mut count: HashMap<char, Vec<i32>> = HashMap::new();
        for c in votes[0].chars() {
            count.insert(c, vec![0; m]);
        }
        for v in &votes {
            for (i, c) in v.chars().enumerate() {
                count.get_mut(&c).unwrap()[i] += 1;
            }
        }
        let mut teams: Vec<char> = count.keys().copied().collect();
        teams.sort_by(|a, b| {
            let ca = &count[a];
            let cb = &count[b];
            for i in 0..m {
                if ca[i] != cb[i] {
                    return cb[i].cmp(&ca[i]);
                }
            }
            a.cmp(b)
        });
        teams.into_iter().collect()
    }
}
