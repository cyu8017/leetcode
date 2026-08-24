// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_good_partitions(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut last = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            last.insert(v, i);
        }
        let mut ans = 1i64;
        let mut end = 0;
        for i in 0..nums.len() {
            if last[&nums[i]] > end {
                end = last[&nums[i]];
            }
            if i == end && i != nums.len() - 1 {
                ans = ans * 2 % MOD;
            }
        }
        ans as i32
    }
}
