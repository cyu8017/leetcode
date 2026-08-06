// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

use std::collections::HashMap;

struct Leaderboard {
    scores: HashMap<i32, i32>,
}

impl Leaderboard {
    fn new() -> Self {
        Self {
            scores: HashMap::new(),
        }
    }

    fn add_score(&mut self, player_id: i32, score: i32) {
        *self.scores.entry(player_id).or_insert(0) += score;
    }

    fn top(&self, k: i32) -> i32 {
        let mut vals: Vec<i32> = self.scores.values().copied().collect();
        vals.sort_unstable_by(|a, b| b.cmp(a));
        vals.into_iter().take(k as usize).sum()
    }

    fn reset(&mut self, player_id: i32) {
        self.scores.remove(&player_id);
    }
}
