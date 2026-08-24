struct Solution;
// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

use std::collections::HashMap;

impl Solution {
    pub fn max_score(prices: Vec<i32>) -> i64 {
        let mut best: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for (i, &p) in prices.iter().enumerate() {
            let key = p - (i as i32 + 1);
            let cand = *best.get(&key).unwrap_or(&0) + p as i64;
            let e = best.entry(key).or_insert(0);
            if cand > *e {
                *e = cand;
            }
            if *e > ans {
                ans = *e;
            }
        }
        ans
    }
}

fn main() {}
