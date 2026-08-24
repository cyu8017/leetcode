// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

use std::collections::HashMap;

impl Solution {
    pub fn destroy_targets(nums: Vec<i32>, space: i32) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *cnt.entry(x % space).or_insert(0) += 1;
        }
        let best_cnt = *cnt.values().max().unwrap();
        let mut ans = 1_000_000_000;
        for (&m, &c) in &cnt {
            if c == best_cnt {
                for &x in &nums {
                    if x % space == m && x < ans {
                        ans = x;
                    }
                }
            }
        }
        ans
    }
}
