// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn min_cost(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let inf = i64::MAX / 4;
        let mut dp = vec![inf; n + 1];
        dp[0] = 0;
        for i in 0..n {
            let mut freq = HashMap::new();
            let mut trimmed = 0i64;
            for j in i..n {
                let c = freq.entry(nums[j]).or_insert(0);
                *c += 1;
                if *c == 2 {
                    trimmed += 2;
                } else if *c > 2 {
                    trimmed += 1;
                }
                let cost = dp[i] + k as i64 + trimmed;
                if cost < dp[j + 1] {
                    dp[j + 1] = cost;
                }
            }
        }
        dp[n] as i32
    }
}
