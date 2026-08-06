// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut frequency = HashMap::new();
        frequency.insert(0, 1);
        let mut odd = 0;
        let mut answer = 0;
        for x in nums {
            odd += x & 1;
            answer += frequency.get(&(odd - k)).copied().unwrap_or(0);
            *frequency.entry(odd).or_insert(0) += 1;
        }
        answer
    }
}
