#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

use std::collections::HashMap;

impl Solution {
    pub fn divisible_triplet_count(nums: Vec<i32>, d: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for j in (i + 1)..n {
                let need = (d - (nums[i] + nums[j]) % d) % d;
                ans += *freq.get(&need).unwrap_or(&0);
                *freq.entry(nums[j] % d).or_insert(0) += 1;
            }
        }
        ans
    }
}
