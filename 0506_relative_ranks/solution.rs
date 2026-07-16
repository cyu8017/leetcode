// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

use std::collections::HashMap;

impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let medals: HashMap<i32, &str> = HashMap::from([
            (1, "Gold Medal"),
            (2, "Silver Medal"),
            (3, "Bronze Medal"),
        ]);
        let mut order: Vec<usize> = (0..score.len()).collect();
        order.sort_by_key(|&index| std::cmp::Reverse(score[index]));

        let mut result = vec![String::new(); score.len()];
        for (rank, index) in order.into_iter().enumerate() {
            let medal_rank = (rank + 1) as i32;
            result[index] = medals
                .get(&medal_rank)
                .map(|label| label.to_string())
                .unwrap_or_else(|| medal_rank.to_string());
        }
        result
    }
}
