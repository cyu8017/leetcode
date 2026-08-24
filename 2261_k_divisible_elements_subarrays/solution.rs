// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

use std::collections::HashSet;

impl Solution {
    pub fn count_distinct(nums: Vec<i32>, k: i32, p: i32) -> i32 {
        let n = nums.len();
        let mut seen = HashSet::new();
        for i in 0..n {
            let mut div = 0;
            let mut key = String::new();
            for j in i..n {
                if nums[j] % p == 0 {
                    div += 1;
                }
                if div > k {
                    break;
                }
                key.push_str(&(nums[j] + 1).to_string());
                key.push(',');
                seen.insert(key.clone());
            }
        }
        seen.len() as i32
    }
}
